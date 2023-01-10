#!/usr/bin/python3
""" A script that adds all args to a python list """


import sys
import os.path

f = __import__('7-save_to_json_file').save_to_json_file
ls = __import__('8-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = ls("add_item.json")

for item in sys.argv[1:]:
    my_list.append(item)

f(my_list, "add_item.json")
