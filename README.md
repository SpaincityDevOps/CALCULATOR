# Calculator

A responsive web calculator built with Flask, vanilla JavaScript, HTML, and CSS. It supports arithmetic sequences, percentages, exponent syntax, keyboard input, and safe server-side expression evaluation.

## GitHub description

Responsive Flask calculator with safe arithmetic evaluation, keyboard support, and a modern dark interface.

## GitHub topics

`calculator` `flask` `python` `javascript` `html` `css` `responsive-design` `web-app` `arithmetic`

## Features

- Responsive layout for mobile, tablet, and desktop screens
- Dark charcoal interface with an orange equals button
- Addition, subtraction, multiplication, division, percentages, and exponents
- Keyboard support, clear, delete, and expression sequences
- Safe AST-based evaluation without Python `eval()`
- Division-by-zero and invalid-expression handling

## Project structure

```text
.
|-- app.py
|-- templates/
|   `-- index.html
|-- static/
|   |-- app.js
|   `-- styles.css
`-- LICENSE
```

## Run locally

1. Create or activate a Python virtual environment.

   ```powershell
   .\calculator\Scripts\Activate.ps1
   ```

2. Install Flask if needed.

   ```powershell
   pip install Flask
   ```

3. Start the application.

   ```powershell
   python app.py
   ```

4. Open http://127.0.0.1:5000 in a browser.

## Contributing

This project is free to use, fork, modify, and redistribute under the MIT License. Bug reports, feature requests, and other issues are welcome through GitHub Issues. Pull requests are welcome as well.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
