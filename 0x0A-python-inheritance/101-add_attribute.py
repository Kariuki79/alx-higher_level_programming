#!/usr/bin/python3
""" Adding module """


def add_attribute(a_class, name, value):
    """ Adds a new attribute """
    if hasattr(a_class, "__dict__"):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")
