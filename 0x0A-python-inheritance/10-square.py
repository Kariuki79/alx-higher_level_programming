#!/usr/bin/python3
"""
Class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of the square"""
    def __init__(self, size):
        """square instantation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns area"""
        return self.__size ** 2
