#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds and returns the biggest integer in a list"""
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for i in my_list:
        if i > biggest:
            biggest = i

    return biggest
