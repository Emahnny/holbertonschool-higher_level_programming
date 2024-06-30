#!/usr/bin/python3
"""
Define the MyList class
"""

class Mylist(list):
    """
    MyList class that ihnerits the list
    """
    def print_sorted(self):
        """
        Print a sorted list
        """
        print(sorted(self))