#!/usr/bin/python3
import json
"""Module that defines a function to load a
Python object from a JSON file."""


def load_from_json_file(filename):
    """Load a Python object from a file in JSON format.

    Args:
        filename (str): The name of the file to load the object from.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
