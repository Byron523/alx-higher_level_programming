#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    size = len(argv)
    if (size - 1) == 0:
        print("{} arguments.".format(size - 1))
    elif (size - 1) == 1:
        print("{} argument: \n{}: {}".format(size - 1, size - 1, argv[1]))
    else:
        print("{} arguments:".format(size - 1))
        for i in range(size - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
