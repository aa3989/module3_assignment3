# Python Command-Line Calculator

A Python calculator with a Read-Eval-Print Loop (REPL), input validation, automated tests, and GitHub Actions.

## Features

- Addition, subtraction, multiplication, and division
- Support for positive numbers, negative numbers, zero, and decimals
- Exact addition, subtraction, and multiplication when both inputs are integers, including large integers
- Whole-number display for exact division results and decimal display for fractional results
- Repeated calculations until the user enters `exit`
- Clear error messages for malformed commands, unknown operations, and division by zero
- Parameterized arithmetic tests with descriptive test IDs
- Required 100% line and branch coverage for `app` and `main.py`

## Setup on Windows with Git Bash

Install Python, Git, and VS Code. The GitHub Actions workflow uses Python 3.14.7.

Clone the repository using its GitHub URL, then enter the project directory.

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

In VS Code, select **Git Bash** as the terminal profile and choose `venv/Scripts/python.exe` through **Python: Select Interpreter**.

## Usage

Start the calculator:

```bash
python main.py
```

Enter commands using this format:

```text
<operation> <first_number> <second_number>
```

Supported operations are `add`, `subtract`, `multiply`, and `divide`.

### Examples

| Command | Output |
|---|---|
| `add 5 3` | `Result: 8` |
| `subtract 10 4` | `Result: 6` |
| `multiply 6 7` | `Result: 42` |
| `add -5 3` | `Result: -2` |
| `add 2.5 3.5` | `Result: 6.0` |
| `divide 20 4` | `Result: 5` |
| `divide 5 2` | `Result: 2.5` |
| `divide 7.5 2` | `Result: 3.75` |
| `add 100000000000000000000000 10000000000000000000` | `Result: 100010000000000000000000` |
| `add 100000000000000000000000 1` | `Result: 100000000000000000000001` |

Use lowercase operation names. Enter `exit` to quit.

### Input Validation and Error Handling

The calculator displays an error message for inputs such as:

```text
add hello 3
add 5
power 2 3
divide 5 0
```

After displaying the error, the calculator prompts for another command.

### Number Handling

The `parse_numbers()` helper converts each input to an integer when possible, preserving large whole numbers without floating-point rounding. Otherwise, it attempts to convert the input to a float.

Division uses `/`, which produces a floating-point result. If that result has no fractional part, the calculator converts it to an integer for display. For example, `5.0` is displayed as `5`, while `2.5` remains `2.5`.

## Project Organization

```text
assignment3/
├── app/
│   ├── __init__.py
│   ├── calculator/
│   │   └── __init__.py
│   └── operations/
│       └── __init__.py
├── tests/
│   ├── test_operations.py
│   ├── test_calculator.py
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .coveragerc
├── .gitignore
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

- `app/operations/__init__.py`: arithmetic functions
- `app/calculator/__init__.py`: REPL, number parsing, input validation, and result display
- `main.py`: application entry point
- `tests/test_operations.py`: parameterized arithmetic tests, including large integers and division by zero
- `tests/test_calculator.py`: user interaction, displayed results, and error handling
- `tests/test_main.py`: application startup behavior
- `pytest.ini` and `.coveragerc`: test discovery and coverage enforcement
- `.github/workflows/tests.yml`: automated testing on GitHub

Arithmetic logic is separated from user interaction to support reuse and independent testing. Parameterized tests avoid repeating the same test logic for different inputs.

## Testing

Run all tests and enforce coverage:

```bash
python -m pytest
```

Show individual test names, including descriptive parameter IDs:

```bash
python -m pytest -v
```

Integer expectations use exact equality to catch precision errors, including an incorrect final digit in a large result. Decimal expectations use `pytest.approx()` to account for small floating-point rounding differences.

Coverage includes both application code in `app` and the `main.py` entry point. The test command fails if any test fails or coverage is below 100%.

Open the HTML coverage report on Windows:

```bash
explorer.exe htmlcov/index.html
```

## Continuous Integration

GitHub Actions installs dependencies and runs the test suite on every push and pull request.

The workflow uses Python 3.14.7 and runs:

```bash
python -m pytest
```

Coverage settings are loaded from the project configuration. Both passing tests and 100% line and branch coverage are required for a successful workflow.

## Limitations

- Decimal inputs use floating-point arithmetic, so some results may contain rounding artifacts.
- Division uses floating-point arithmetic, so very large quotients may lose precision. Converting a whole-number quotient to an integer changes its display but does not restore lost precision.
- Exact integer arithmetic applies to addition, subtraction, and multiplication when both inputs are entered as integers.