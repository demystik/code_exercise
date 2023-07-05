#!/usr/bin/python3
def convert_add(List):
    """convert_add that takes a list of strings
    as an argument and converts it to integers and sums the list. For
    example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
    summed to 9.
    """
    total = 0
    for num in List:
        total += int(num)
    return total

test_list = [1, 3, 5]
convert_add(test_list)
