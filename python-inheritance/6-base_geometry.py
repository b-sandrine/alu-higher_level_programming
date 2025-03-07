#!/usr/bin/python3
""" Empty class """


class BaseGeometry:
    """Raises exception when area is called"""

    def area(self):
        """ Raising an exception usnign Exception """

        raise Exception("area() is not implemented")
