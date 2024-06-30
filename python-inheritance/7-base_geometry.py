#!/usr/bin/python3

class BaseGeometry:

    """
    Base Geometry class
    """

    def area(self):
        """
        Calculate the area of a geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")