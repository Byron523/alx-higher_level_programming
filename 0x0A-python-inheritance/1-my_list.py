#!/usr/bin/python3
class MyList(list):
    """ Class that inherits attributes of a class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Prints a sorted list """
        sorte = self.copy()
        sorte.sort()
        print(sorte)
