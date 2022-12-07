#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    d = 0

    for item in my_list:
        num += item[0] * item[1]
        d += item[1]

    return (num / d)
