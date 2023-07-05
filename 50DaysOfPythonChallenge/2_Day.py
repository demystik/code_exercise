#!/usr/bin/python3
def convert_add(List):
    total = 0
    for num in List:
        total += int(num)
    return total

test_list = [1, 3, 5]
convert_add(test_list)
