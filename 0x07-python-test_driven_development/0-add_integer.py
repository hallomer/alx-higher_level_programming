#!/usr/bin/python3
"""Adds two numbers."""


def add_integer(a, b=98):
    """
    Parameters:
    a (int or float): The first number to be added.
    b (int or float): The second number to be added. Default value is 98.

    Raises:
    TypeError: If either `a` or `b` is not an integer or float.

    Returns:
    int: The sum of `a` and `b`.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
