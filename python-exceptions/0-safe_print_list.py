#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements from my_list safely and returns the count printed."""
    count = 0  # Tracks the number of elements printed
    try:
        for i in range(x):  # Loop through x times
            print(my_list[i], end="")  # Print elements on the same line
            count += 1  # Increment the count
    except IndexError:  # If x > list length, catch the error and exit the loop
        pass
    print()  # Newline after printing elements
    return count  # Return actual number of elements printed
