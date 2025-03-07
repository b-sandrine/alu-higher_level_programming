#!/usr/bin/python3
'''BaseGeometry class with methods for area calculation and integer validation.'''


class BaseGeometry:
    '''A base class for geometry-related operations.'''

    def area(self):
        '''Raises an exception indicating the method is not implemented.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates that value is an integer and greater than 0.
        
        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
