#!/usr/bin/python3
import json
"""Module that defines a function to save a
Python object to a JSON file."""


def save_to_json_file(my_obj, filename):
    """Save a Python object to a file in JSON format.

    Args:
        my_obj (object): The Python object to be saved.
        filename (str): The name of the file where the
        object will be saved.
    """
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
