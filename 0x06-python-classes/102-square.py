#!/usr/bin/python3

class Square:
    """
    Represents a square shape.

    Attributes:
        __size (float): The size of the square.

    Methods:
        __init__(size=0): Initializes a new instance of the Square class.
        size(): Getter method for the size attribute.
        size(value): Setter method for the size attribute.
        area(): Calculates and returns the area of the square.
        __lt__(other): Less than comparison operator overload.
        __le__(other): Less than or equal to comparison operator overload.
        __eq__(other): Equality comparison operator overload.
        __ne__(other): Not equal to comparison operator overload.
        __gt__(other): Greater than comparison operator overload.
        __ge__(other): Greater than or equal to comparison operator overload.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
