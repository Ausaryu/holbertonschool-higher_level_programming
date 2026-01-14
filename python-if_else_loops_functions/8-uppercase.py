#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(0, len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            result += chr(ord(str[i]) - 32)
        else:
            result += str[i]
    print("{}".format(result))
    return result
