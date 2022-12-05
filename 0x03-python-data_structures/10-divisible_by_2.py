#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for item in my_list:
        if (item % 2) != 0:
            new.append(False)
        else:
            new.append(True)
    return (new)
