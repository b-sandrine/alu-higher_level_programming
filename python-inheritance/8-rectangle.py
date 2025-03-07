#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''Initializes a rectangle with width and height, validating them'''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
