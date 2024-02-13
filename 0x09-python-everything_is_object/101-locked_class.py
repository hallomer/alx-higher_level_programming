#!/usr/bin/python3
"""this is a class."""


class LockedClass:
    """
    Allows only the 'first_name' attribute to be created.
    """
    __slots__ = ['first_name']
