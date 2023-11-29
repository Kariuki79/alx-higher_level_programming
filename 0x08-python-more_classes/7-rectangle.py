#!/usr/bin/python3
"""
Module: 7-rectangle
Defines a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle class
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns a string representation """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ((str(self.print_symbol) *self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """
        Rectangle string representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of Rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
