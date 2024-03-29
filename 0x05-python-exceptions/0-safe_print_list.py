#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of the list

    Args:
        my_list (list): The list to print elements
        x (int): The number of elements of my_list to print

    Returns:
        The real number of elements printed
    """
    rt = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            rt += 1
        except IndexError:
            break
    print("")
    return (rt)
