#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
        new = []
        if idx > len(my_list) or idx < 0:
                return (my_list)
        else:
                for item in my_list:
                        for i in range(len(my_list)):
                                if i == idx:
                                        del my_list[idx]
                                else:
                                        new.append(item)
                return (new)