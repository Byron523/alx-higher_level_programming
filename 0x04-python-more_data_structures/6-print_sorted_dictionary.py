#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = list(a_dictionary.keys())
    ls.sort()
    for item in ls:
        print("{}: {}".format(item, a_dictionary.get(i)))
