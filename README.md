Here's a comprehensive README.md for both projects:

```markdown
# Python Learning Projects

This repository contains two separate projects demonstrating different Python concepts:

## 1. Django Signals Demo

### Overview
A Django project demonstrating the behavior of Django signals with respect to:
- Synchronicity
- Threading
- Transaction management

### Questions Explored
1. **Signal Synchronicity**
   - Question: Are Django signals executed synchronously or asynchronously by default?
   - Implementation: See core/models.py (lines 15-19) and core/tests.py (lines 8-12)
   - Test: `test_synchronous_signal` demonstrates synchronous execution with time stamps

2. **Signal Threading**
   - Question: Do Django signals run in the same thread as the caller?
   - Implementation: See core/models.py (lines 21-24) and core/tests.py (lines 14-18)
   - Test: `test_signal_thread` compares thread names

3. **Signal Transactions**
   - Question: Do Django signals run in the same database transaction as the caller?
   - Implementation: See core/models.py (lines 26-28) and core/tests.py (lines 20-24)
   - Test: `test_signal_transaction` verifies transaction state

### Running the Django Project
1. Navigate to the project directory:
```bash
cd Django_Signals/signals_demo
```
2. Run migrations:
```bash
python manage.py migrate
```
3. Run tests:
```bash
python manage.py test core.tests.SignalTests -v 2
```

## 2. Python Custom Classes - Rectangle Iterator

### Overview
Demonstrates Python's iterator protocol implementation using a Rectangle class.

### Requirements
- Rectangle class must be initialized with length and width (both integers)
- Must be iterable
- Iterator should return:
  1. First iteration: `{'length': <VALUE>}`
  2. Second iteration: `{'width': <VALUE>}`

### Project Structure
```
python_custom_classes/
├── src/
│   ├── __init__.py
│   └── rectangle.py
└── tests/
    ├── __init__.py
    └── test_rectangle.py
```

### Running the Rectangle Project
1. Navigate to the project directory:
```bash
cd python_custom_classes
```
2. Run tests:
```bash
python tests/test_rectangle.py
```

### Example Usage
```python
from src.rectangle import Rectangle

rect = Rectangle(5, 3)
for dimension in rect:
    print(dimension)
# Output:
# {'length': 5}
# {'width': 3}
```

## Development Setup
- Python 3.8+
- Django 5.1+ (for signals demo)
- No additional requirements for Rectangle project

## Contributing
Feel free to submit issues and enhancement requests.

## License
MIT License
```
