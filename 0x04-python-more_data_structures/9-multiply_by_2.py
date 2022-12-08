#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    ls = list(new.keys())

    for item in ls:
        new[item] *= 2

    return (new)
