#!/usr/bin/python3

import math
def divide_or_square(num):
    """takes one
    argument (a number), and returns the square root of the number
    if it is divisible by 5, returns its remainder if it is not divisible by
    5. For example, if you pass 10 as an argument, then your function
    should return 3.16 as the square root.
    """
    return f'{math.sqrt(num):.2f}' if num % 5 == 0 else num % 5

number = 10
print(divide_or_square(number))
