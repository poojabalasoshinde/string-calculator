# String Calculator – TDD Kata (Python)

This is a complete implementation of the classic [String Calculator Kata] using **Test-Driven Development** in Python.

All phases from basic addition to custom delimiters, negative number validation, and advanced delimiter parsing are covered.

---

## Features Implemented

- Add 0, 1, or more comma-separated numbers
- Support for newline (`\n`) as a delimiter
- Custom single-character delimiters (`//;\n1;2`)
- Custom multi-character delimiters (`//[***]\n1***2`)
- Multiple delimiters (`//[*][%]\n1*2%3`)
- Negative number detection with full error list
- Ignore numbers > 1000
- Count how many times `add()` is called
- 100% test coverage using `pytest`

---

## Tech Stack

- Python 3.11+
- `pytest` for testing
- `pytest-cov` for coverage
- TDD cycle: Red → Green → Refactor

---

## Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/string-calculator-tdd.git
cd string-calculator-tdd


## 2.  Install dependencies
pip install -r requirements.txt

## 3. Run tests
PYTHONPATH=. pytest

## 4. Run with coverage
pytest --cov=string_calculator


## Project Structure
string_calculator/
├── __init__.py
├── string_calculator.py
tests/
├── __init__.py
├── test_string_calculator.py


