#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        if idx < 0 or idx > len(my_list):
                return (my_list)
        else:
                new = []
                for i in my_list:
                        if (i - 1) != idx:
                                new.append(i)
                        else:
                                new.append(element)
                return (new)
