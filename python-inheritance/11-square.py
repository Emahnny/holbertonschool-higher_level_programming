#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):

        """
         Square  inherits from Rectangle
        Attributes:
            size (int): side of square
        Methods:
            __init__ - initialises the square
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

        def __str__(self):
            """
            Return a string representation of the square
            """
            return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))