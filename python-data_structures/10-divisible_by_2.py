#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a list of True/False indicating if elements are divisible by 2."""
    return [num % 2 == 0 for num in my_list]
