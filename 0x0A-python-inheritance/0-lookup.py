#!/usr/bin/python3
"""
Contains the lookup function that returns the list of variables
"""


def lookup(obj):
    """returns a list of available attributes"""
    return dir(obj)
