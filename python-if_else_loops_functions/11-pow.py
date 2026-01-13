#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(0, b):
            result *= a
    elif b == 0:
        result = 1
    else:
        for i in range(0, abs(b)):
            result = result / a
    return result
