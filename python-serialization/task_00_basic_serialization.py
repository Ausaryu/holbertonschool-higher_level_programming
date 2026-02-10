#!/usr/bin/env python3
from json import loads, dumps

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "w",encoding="utf-8") as f:
        f.write(dumps(data))

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, encoding="utf-8") as f:
        return loads(f.read())