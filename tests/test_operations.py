import pytest

from app.operations import addition, subtraction, multiplication, division
@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (addition, 2, 3, 5),
        (addition, -2, -3, -5),
        (addition, 0, 7, 7),
        (addition, 0.1, 0.2, 0.3),
        (subtraction, 5, 2, 3),
        (subtraction, 2, 5, -3),
        (subtraction, -2, -3, 1),
        (subtraction, 0, 0, 0),
        (multiplication, 4, 5, 20),
        (multiplication, -4, 5, -20),
        (multiplication, 0, 5, 0),
        (multiplication, 1.5, 2, 3),
        (division, 10, 2, 5),
        (division, -10, 2, -5),
        (division, 0, 2, 0),
        (division, 1, 4, 0.25),
        (
            addition,
            100000000000000000000000,
            10000000000000000000,
            100010000000000000000000,
        ),
        (
            addition,
            100000000000000000000000,
            1,
            100000000000000000000001,
        ),
    ],
    ids=[
        "Add Positive Numbers",
        "Add Negative Numbers",
        "Add Zero",
        "Add Decimals",
        "Subtract Positive Result",
        "Subtract Negative Result",
        "Subtract Negative Numbers",
        "Subtract Zeros",
        "Multiply Positive Numbers",
        "Multiply Negative and Positive",
        "Multiply by Zero",
        "Multiply Decimals",
        "Divide Positive Numbers",
        "Divide Negative and Positive",
        "Divide Zero Numerator",
        "Divide Fractional Result",
        "Add Large Integers",
        "Preserve Last Digit",
    ],
)

def test_operations(operation, a, b, expected):
    """Test basic arithmetic operations, including exact handling of large integers results."""
    result = operation(a, b)
    if isinstance(expected, int):
        assert result == expected
    else:
        assert result == pytest.approx(expected)

@pytest.mark.parametrize("numerator", [0, 1, -1, 2.5],
ids=[
    "Zero divided by Zero",
    "Positive divided by Zero",
    "Negative divided by Zero", 
    "Decimal divided by Zero",
    ],
)

def test_division_by_zero(numerator):
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(numerator, 0)

# def test_addition():
#     assert addition(1, 1) == 2
    
# def test_subtraction():
#     assert subtraction(1, 1) == 0

# def test_multiplication():
#     assert multiplication(1, 1) == 1

# def test_division_positive():
#     assert division(1, 1) == 1

# def test_division_by_zero():
#     """Test division by zero."""
#     with pytest.raises(ValueError, match="Division by zero is not allowed."):
#         division(1, 0)
