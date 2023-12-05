#!/usr/bin/python3
"""
same_class function that returns true
"""


def is_same_class(obj, a_class):
    """return true if object is exactly an instance of the specified class"""
    return (type(obj) == a_class)
