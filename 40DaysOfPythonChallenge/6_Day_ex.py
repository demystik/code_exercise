#!/usr/bin/python3

def zeroed(list_of_num):
    """zeroed code that takes a list of numbers
    as an argument. The code should zero (0) the first and the last
    number in the list
    """
    list_of_num[0] = 0
    list_of_num[-1] = 0
    return list_of_num


print(zeroed([2, 5, 7, 8, 9]))
