#!/usr/bin/python3
"""
Module that defines a function to print text with
two new lines after '.', '?', and ':' characters,
with no leading or trailing spaces on lines.
"""


def text_indentation(text):
    """
    Prints the given text with two new lines
    after each '.', '?', and ':'.
    Args:
        text (str): The text to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print()  # first newline
            if i != length - 1:
                print()  # second newline only if not last char
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
