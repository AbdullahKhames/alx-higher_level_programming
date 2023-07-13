#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""


import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
ls = []
try:
    ls = load_from_json_file(filename)
except json.JSONDecodeError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
for item in  sys.argv[1:]:
    ls.append(item)
save_to_json_file(ls, filename)
print(ls)
