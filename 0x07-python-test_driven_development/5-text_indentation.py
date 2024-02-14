#!/usr/bin/python3
"""Prints the given text with indentation."""


def text_indentation(text):
    """
    Parameters:
    text (str): The text to be indented.

    Raises:
    TypeError: If `text` is not a string.

    Returns:
    None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    add_space = True
    new_text = ""
    for i in range(0, len(text)):
        if text[i] not in [" ", '\t']:
            add_space = True
        if add_space:
            new_text += text[i]
        if text[i] in [".", "?", ":"]:
            print(new_text, end="\n\n")
            add_space = False
            new_text = ""
