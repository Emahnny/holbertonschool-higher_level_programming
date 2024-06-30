#!/usr/bin/python3
"""
    Define the MyList class
"""

class Mylist(list):
    """
        This class inherits from list.
        Attributes:
        Methods:
            print_sorted - prints the list in ascending order
    """
    def print_sorted(self):
        """
            Print a sorted list
        """
        print(sorted(self))




