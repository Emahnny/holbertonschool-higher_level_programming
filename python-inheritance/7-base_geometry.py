#!/usr/bin/python3

class BaseGeometry:

    """
    Base Geometry class
    """

    def area(self):
        """
                BaseGeometry
        Attributes: None.
        Methods:
            area() - raises an Exception
            integer_validator() - validates value.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
         integer_validator checks the value of value.
            Args:
                name (str): name
                value (int): value
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")