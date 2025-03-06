---
layout: default
title: Python Project Exercise
permalink: /git_software_dev_workshop/exercises/python_project/
progress: 100
previous: /git_software_dev_workshop/04_project_management/02_workflow_strategies/
---

# Python Project Exercise

This exercise will help you practice Git concepts by working on a simple Python project.

## Project Setup

1. Create a new directory for the project:
```bash
mkdir python-git-exercise
cd python-git-exercise
```

2. Initialize a Git repository:
```bash
git init
```

3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Create a requirements.txt file:
```bash
echo "pytest==7.4.0" > requirements.txt
pip install -r requirements.txt
```

## Project Structure

Create the following files:

1. `calculator.py`:
```python
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
```

2. `test_calculator.py`:
```python
import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)
```

## Exercise Tasks

1. **Initial Setup**
   - Create the project structure
   - Initialize Git repository
   - Create and activate virtual environment
   - Install dependencies

2. **Basic Git Operations**
   - Add all files to Git
   - Create initial commit
   - Create a new branch for feature development

3. **Feature Development**
   - Add new calculator functions (power, square root)
   - Write corresponding tests
   - Commit changes
   - Merge feature branch

4. **Collaboration Practice**
   - Create a new branch for bug fixes
   - Fix a bug in the calculator
   - Write test for the fix
   - Create pull request

5. **Advanced Git Operations**
   - Create a release tag
   - Revert a commit
   - Cherry-pick a commit
   - Resolve merge conflicts

## Running Tests

```bash
pytest test_calculator.py -v
```

## Expected Outcomes

1. Working calculator implementation
2. Passing test suite
3. Clean Git history
4. Understanding of Git workflow
5. Experience with collaboration

## Additional Challenges

1. Add more mathematical operations
2. Implement error handling
3. Add documentation
4. Create a command-line interface
5. Add performance tests

## Resources

- [Python Documentation](https://docs.python.org/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Git Documentation](https://git-scm.com/doc) 