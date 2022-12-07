#!/usr/bin/python3
def uniq_add(my_list=[]):
    one_only = set(my_list)
    number = 0

    for item in one_only:
        number += item
    return (number)
