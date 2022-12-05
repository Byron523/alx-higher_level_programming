#!/usr/bin/python3
def no_c(my_string):
        c = ''
        for item in my_string:
                if item == 'C' or item == 'c':
                        pass
                else:
                        c = c + item
        return (c)
