#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):

        """
        Rectangle class
        """

        def __init__(self, width, height):
            """
            Initialize a rectangle
            """
            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.__width = width
            self.__height = height

        def area(self):
            """
            Calculate the area of a rectangle
            """
            return self.__width * self.__height

        def __str__(self):
            """
            Return a string representation of a rectangle
            """
            return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


