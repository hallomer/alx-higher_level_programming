#!/usr/bin/python3

"""Represents a square shape with a size."""


class Square:
    """
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(size=0): Initializes a new instance of the Square class.
        size(): Getter method for the size attribute.
        size(value): Setter method for the size attribute.
        area(): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
