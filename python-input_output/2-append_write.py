#!/usr/bin/python3
"""Module for appending text to files"""


def append_write(filename="", text=""):
    """function for appending text to files"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
