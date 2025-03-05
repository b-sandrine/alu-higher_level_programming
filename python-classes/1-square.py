#!/usr/bin/python3
"""Module for creating square class with a private attribute"""


class Square:
    """Adding a private attribute size"""
    def __init__(self, size):
        self.__size = size # Private attribute
