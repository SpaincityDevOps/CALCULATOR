const display = document.getElementById('display');
const keypad = document.querySelector('.keypad');
let calculating = false;

async function calculate() {
    if (!display.value || calculating) return;

    calculating = true;
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ expression: display.value })
        });
        if (!response.ok) throw new Error('Calculation failed');
        const data = await response.json();
        display.value = data.result;
    } catch {
        display.value = 'Error';
    } finally {
        calculating = false;
    }
}

function appendValue(value) {
    if (display.value === 'Error') display.value = '';
    display.value += value;
}

keypad.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button) return;

    const { action, value } = button.dataset;
    if (action === 'clear') display.value = '';
    else if (action === 'delete') display.value = display.value.slice(0, -1);
    else if (action === 'calculate') calculate();
    else if (value) appendValue(value);
});

document.addEventListener('keydown', event => {
    if (/^[0-9.+\-*/%^]$/.test(event.key)) {
        event.preventDefault();
        appendValue(event.key);
    } else if (event.key === 'Enter' || event.key === '=') {
        event.preventDefault();
        calculate();
    } else if (event.key === 'Escape') {
        display.value = '';
    } else if (event.key === 'Backspace') {
        display.value = display.value.slice(0, -1);
    }
});