import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rectangle import Rectangle

# Create and use a rectangle
rect = Rectangle(5, 3)
for dimension in rect:
    print(dimension)

def test_basic_iteration():
    # Test case 1: Basic iteration
    rect = Rectangle(5, 3)
    dimensions = list(rect)
    assert dimensions == [{'length': 5}, {'width': 3}]
    print("Test 1 passed: Basic iteration works")

def test_multiple_iterations():
    # Test case 2: Multiple iterations
    rect = Rectangle(4, 2)
    first_iteration = list(rect)
    second_iteration = list(rect)
    assert first_iteration == second_iteration
    print("Test 2 passed: Multiple iterations work")

def test_type_checking():
    # Test case 3: Type checking
    rect = Rectangle(10, 7)
    for item in rect:
        assert isinstance(item, dict)
    print("Test 3 passed: Return types are dictionaries")

if __name__ == "__main__":
    test_basic_iteration()
    test_multiple_iterations()
    test_type_checking()