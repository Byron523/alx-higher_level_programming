#!/usr/bin/python3
""" A class that int """

class MyInt(int):
    """ MyInt inherits a class called int """

    def __eq__(self, other):
        """ a method that return != check """
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """ a method that returns == back """
        return (int.__eq__(self, other))
