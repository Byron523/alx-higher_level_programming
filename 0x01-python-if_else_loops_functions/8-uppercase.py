#!/usr/bin/python3
def uppercase(str):
    for i in str:
        s = chr(ord(i) - 32)
        print("{}".format(s), end='')
    print()
