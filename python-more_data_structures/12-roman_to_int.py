#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or None:
        return 0
    roman_digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                   'D': 500, 'M': 1000}
    old_value = 0
    result = 0
    for i in reversed(roman_string):
        value = roman_digit.get(i, 0)
        if value >= old_value:
            result += value
            old_value = value
        else:
            result -= value
    return result
