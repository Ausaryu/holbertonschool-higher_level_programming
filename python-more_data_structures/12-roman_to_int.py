#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or None:
        return
    positive_i = True
    positive_V = True
    positive_X = True
    positive_L = True
    positive_C = True
    positive_D = True
    result = 0
    for i in reversed(roman_string):
        if positive_i is True and i == 'I':
            result += 1
        if positive_i is False and i == 'I':
            result -= 1
        elif positive_V is True and i == 'V':
            result += 5
            positive_i = False
        elif positive_V is False and i == 'V':
            result -= 5
        elif positive_X is True and i == 'X':
            result += 10
            positive_i = False
            positive_V = False
        elif positive_X is False and i == 'X':
            result -= 10
        elif positive_L is True and i == 'L':
            result += 50
            positive_i = False
            positive_V = False
            positive_X = False
        elif positive_L is False and i == 'L':
            result -= 50
        elif positive_C is True and i == 'C':
            result += 100
            positive_i = False
            positive_V = False
            positive_X = False
            positive_L = False
        elif positive_C is False and i == 'C':
            result -= 100
        elif positive_D is True and i == 'D':
            result += 500
            positive_i = False
            positive_V = False
            positive_X = False
            positive_L = False
            positive_C = False
        elif positive_D is False and i == 'D':
            result -= 500
        elif i == 'M':
            result += 1000
            positive_i = False
            positive_V = False
            positive_X = False
            positive_L = False
            positive_C = False
            positive_D = False
    return result
