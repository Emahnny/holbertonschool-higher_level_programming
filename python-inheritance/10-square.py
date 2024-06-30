#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):

        """
        Square class
        """

        def __init__(self, size):
            """
            Initialize a square
            """
            self.integer_validator("size", size)
            self.__size = size
            super().__init__(size, size)

        def area(self):
            """
            Calculate the area of a square
            """
            return self.__size ** 2

       