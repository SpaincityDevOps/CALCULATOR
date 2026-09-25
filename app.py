from flask import Flask, jsonify, render_template, request
import ast
import math
import operator
import re

app = Flask(__name__)

MAX_EXPRESSION_LENGTH = 200
PERCENTAGE_PATTERN = re.compile(r"(?<![\w.])((?:\d+(?:\.\d*)?|\.\d+))%")


def safe_eval(expr):
    """Evaluate the calculator's limited arithmetic grammar without eval()."""
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos
    }

    try:
        if not isinstance(expr, str) or not expr.strip() or len(expr) > MAX_EXPRESSION_LENGTH:
            raise ValueError("Invalid expression")

        normalized = expr.replace('^', '**')
        normalized = PERCENTAGE_PATTERN.sub(r'(\1 / 100)', normalized)
        node = ast.parse(normalized, mode='eval')

        def _eval(node):
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.BinOp):
                operation = operators.get(type(node.op))
                if operation is None:
                    raise TypeError("Unsupported operation")
                left = _eval(node.left)
                right = _eval(node.right)
                if isinstance(node.op, ast.Pow) and abs(right) > 1000:
                    raise ValueError("Exponent is too large")
                value = operation(left, right)
            elif isinstance(node, ast.UnaryOp):
                operation = operators.get(type(node.op))
                if operation is None:
                    raise TypeError("Unsupported operation")
                value = operation(_eval(node.operand))
            elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
                value = node.value
            else:
                raise TypeError("Unsupported operation")

            if not math.isfinite(value):
                raise ValueError("Result is not finite")
            return value

        result = _eval(node)
        return int(result) if isinstance(result, float) and result.is_integer() else result
    except Exception:
        return "Error"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}
    result = safe_eval(data.get("expression", ""))
    return jsonify({"result": str(result)})

if __name__ == "__main__":
    app.run()
