#!/usr/bin/python3

def no_c(my_string):
    if not my_string:
        return ""
    return "".join(char for char in my_string if char not in "cC")
