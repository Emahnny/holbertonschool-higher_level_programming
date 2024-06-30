"""
    4-inherits_from: inherits_from()
"""

def inherits_from(obj, a_class):
    """
    inherits_from returns True if the object is an instance of the specified class
    and not the same class.

    Args:
        obj (object): Object to check.
        a_class (class): Class to compare against.

    Returns:
        bool: True if object is an instance of the specified class and not the same class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)