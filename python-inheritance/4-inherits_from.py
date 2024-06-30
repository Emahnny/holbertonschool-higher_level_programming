#!/usr/bin/python3

def inherit_from(obj, a_class):
    """
        inherits_from returns true if object is instance of a class
        that inherited directly or indirectly from the specified class.
        Args:
            obj (object): object.
            a_class (class): class.
        Returns: True or False.
    """
    return issubclass(type(obj), a_class)