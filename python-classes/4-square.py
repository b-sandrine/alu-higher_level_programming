#!/usr/bin/python3
"""Module for creating square class with a private attribute"""


class Square:
    """Adding a private attribute size and instantiating it"""
    def __init__(self, size=0):

        self.size = size  # Calls the setter function to set the size

    # Adding setter and getter

    @property
    def size(self):
            
        """ Size property for getting size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Adding exceptions to check if size is type int and if it is
            not less that zero """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value   # Setting size to value

    # Public function for finding area
    def area(self):
        """ Returns the current area of the square """
        return self.__size ** 2
