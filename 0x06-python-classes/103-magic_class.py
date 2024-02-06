#!/usr/bin/python3
"""this is a magic class"""
import math


class MagicClass:
    """Represents a magical shape with a radius."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass."""
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the magical shape."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the magical shape."""
        return 2 * math.pi * self.__radius
