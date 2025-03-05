#!/usr/bin/python3
"""Module for creating square class with a private attribute"""


class Square:
    """Adding 2 private attributes size and position and instantiating them"""
    def __init__(self, size=0, position=(0, 0)):

        self.size = size  # Calls the setter function to set the size
        self.position = position

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

    # Setter and getters for position attribute

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    # Public function for finding area
    def area(self):
        """ Returns the current area of the square """
        return self.__size ** 2

    # Function for printing square with #
    def my_print(self):
        """Prints on the STDOUT the square depending on the size"""
        if self.size == 0:
            print("")
        else:
            # Printing vertical spasing based on position[1]
            print("\n" * self.__position[1], end="")

            # Print square with leading spaces
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
