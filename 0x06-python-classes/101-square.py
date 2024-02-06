#!/usr/bin/python3

class Square:
    """
    Represents a square shape with a size and position.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(size=0, position=(0, 0)):
              Initializes a new instance of the Square class.
        size(): Getter for the size attribute.
        size(value): Setter for the size attribute.
        position(): Getter for the position attribute.
        position(value): Setter for the position attribute.
        area(): Calculates and returns the area of the square.
        my_print(): Prints a visual representation of the square.
        __str__(): Returns a string representation of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints a visual representation of the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        if self.size == 0:
            return ""
        square_str = ""
        for _ in range(self.position[1]):
            square_str += "\n"
        for _ in range(self.size):
            square_str += " " * self.position[0] + "#" * self.size + "\n"
        return square_str
