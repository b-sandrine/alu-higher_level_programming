#!/usr/bin/python3
class MyList(list):
    """A subclass of list that includes a method to print a sorted version of the list."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
