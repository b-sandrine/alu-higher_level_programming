#!/usr/bin/python3
""" Empty class """


class BaseGeometry:
    """Raises exception when area is called"""

    def area(self):
        """ Raising an exception usnign Exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
    """ Method which validates value variable """
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
