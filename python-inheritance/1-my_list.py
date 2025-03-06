#!/usr/bin/bash
"""class MyList that inherits from list"""


class MyList(list):
    """A subclass of list with a method to print a sorted version of the list."""

    def print_sorted(self):
        """Prints in the ascending order"""
        print(sorted(self))
