#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for i in range(len(my_list)):
        check = False
        for y in range(i+1, len(my_list)):
            if my_list[y] == my_list[i]:
                check = True
        if check is False:
            result += my_list[i]
    return result
