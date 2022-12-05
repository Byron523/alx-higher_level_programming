#!/usr/bin/python3
def max_integer(my_list=[]):
        top = 0
        for item in my_list:
                if item > top:
                        top = item
        return (top)
