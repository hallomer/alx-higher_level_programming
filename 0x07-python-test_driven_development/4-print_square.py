#!/usr/bin/python3
"""Prints a square made of '#' characters with a given size."""


def print_square(size):
    """
    Parameters:
    size (int): The size of the square.

    Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than zero.

    Returns:
    None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
    print()
