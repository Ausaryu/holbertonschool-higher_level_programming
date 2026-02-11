#!/usr/bin/python3
"""
This script adds command-line arguments to a list stored in a JSON file.
If the file does not exist, it is created automatically.
"""

from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []

for i in range(1, len(argv)):
    my_list.append(argv[i])

save_to_json_file(my_list, filename)
