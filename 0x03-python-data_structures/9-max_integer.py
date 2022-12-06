#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    top = 0
    for item in my_list:
        if item > top:
            top = item
    return (top)
