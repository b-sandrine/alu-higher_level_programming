#!/usr/bin/python3
"""Module for creating square class with a private attribute"""


class Square:
    """Adding a private attribute size and instantiating it"""
    def __init__(self, size=0):

        """Adding exceptions to check if size is type int and if it is
        not less that zero """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size   # Private attribute

    # Public function for finding area
    def area(self):
        """ Returns the current area of the square """
        return self.__size ** 2
