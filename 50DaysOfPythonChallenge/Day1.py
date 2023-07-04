#!/usr/bin/python3

import math
def divide_or_square(num):
    return math.sqrt(num) if num % 5 == 0 else num % 5

number = 10
print(divide_or_square(number))
