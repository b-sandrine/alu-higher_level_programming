#!/usr/bin/python3
'''Class Square that inherits from Rectangle (9-rectangle.py)'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle'''

    def __init__(self, size):
        '''Initializes a square with size, validating it'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Returns the area of the square'''
        return self.__size * self.__size
