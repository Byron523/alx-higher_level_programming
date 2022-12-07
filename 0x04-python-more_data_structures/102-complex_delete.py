#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lis = list(a_dictionary.keys())

    for item in lis:
        if value == a_dictionary.get(item):
            del a_dictionary[item]
    return (a_dictionary)
