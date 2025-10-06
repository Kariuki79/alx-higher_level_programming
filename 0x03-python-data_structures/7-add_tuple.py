#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuple and returns a new tuples with 2 integers"""
    # Extend both tuples to have at least 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Add the first and second elements
    return (a[0] + b[0], a[1] + b[1])

