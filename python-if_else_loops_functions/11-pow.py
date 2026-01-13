#!/usr/bin/python3
def pow(a, b):
    result = a
    if b > 0:
        for i in range(1, b):
            result *= a
    elif b == 0:
        result = 1
    else:
        for i in range(1, abs(b)):
            result = result / a
    return result
