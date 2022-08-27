"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

import os
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Compute and return the sum of two numbers.

    Examples:
        >>> add(2.0, 3.0)
        5.0
        >>> add(1, 2)
        3.0

    Args:
        a (float): a number represent first addend in the addition
        b (float): a number represent second addend in the addition

    Returns:
        float: a number representing the arithmic sum of 'a' and 'b'
    """
    return float(a+b)

def substract(a, b):
    return float(a - b)

def multiply(a, b):
    return float(a * b)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a/b)


    