#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
ls = []
for count, item in enumerate(sys.argv):
    if count == 0:
        continue
    ls.append(item)
other_ls = []
try:
    other_ls = load_from_json_file(filename)
except json.JSONDecodeError as e:
    print(e)
if type(other_ls) is list and len(other_ls) != 0:
    ls.extend(other_ls)
save_to_json_file(ls, filename)
print(ls)
