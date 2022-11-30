#!/usr/bin/python3
def uppercase(str):
    for i in str:
        s = chr(ord(i) - 32)
        print(f"{s}", end='')
    print()
