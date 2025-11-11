#!/usr/bin/python3
"""Module that defines the MyList class"""


class MyList(list):
    """MyList class that inherits from list

    This class extends the built-in list class with additional functionality
    to print a sorted version of the list.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order

        This method prints a sorted copy of the list without modifying
        the original list. Assumes all elements are integers.
        """
        print(sorted(self))
