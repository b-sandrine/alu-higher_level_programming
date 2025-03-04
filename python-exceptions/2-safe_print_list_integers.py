#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for count in range(x):
            try:
                print("{:d}".format(my_list[count]), end="")
                count += 1
            except (TypeError, ValueError):
                continue
    except(IndexError):
        pass
    print()
    return count
