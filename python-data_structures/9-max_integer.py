#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the maximum integer in a list."""
    if not my_list:
        return None
    
    max_num = my_list[0]  # Assume the first element is the max
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num
