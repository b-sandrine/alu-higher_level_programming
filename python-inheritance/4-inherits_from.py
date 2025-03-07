#!/usr/bin/python3
"""returns True if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """that inherited from the specified class"""

    return isinstance(obj, a_class) and type(obj) != a_class
