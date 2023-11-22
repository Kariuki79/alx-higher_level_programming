#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
     """A function that prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements
        x (int): The number of elements of my_list that will print

    Returns:
        Real number of integers printed
    """
    a = 0
    for b in range(0, x):
        try:
            print("{:d}".format(my_list[b]), end="")
            a += 1
        except(ValueError, TypeError):
            continue
    print("")
    return (a)
