#!/usr/bin/python3
"""
Function inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """returns true if the object is an instance of a class"""
      return False if type(obj) == a_class else isinstance(obj, a_class)
