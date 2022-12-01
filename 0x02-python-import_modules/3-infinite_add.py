#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    a = len(argv)
    for i in range(a - 1):
        add = add + int(argv[i + 1])
    print("{}".format(add))
