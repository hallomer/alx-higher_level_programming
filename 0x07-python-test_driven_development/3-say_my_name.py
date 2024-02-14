#!/usr/bin/python3
"""Prints a person's name."""


def say_my_name(first_name, last_name=""):
    """
    Parameters:
    first_name (str): The first name of the person.
    last_name (str, optional): The last name of the person.
    Default value is an empty string.

    Raises:
    TypeError: If `first_name` is not a string.
    TypeError: If `last_name` is not a string.

    Returns:
    None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
