#!/usr/bin/env python3

first = int(input("Enter fist integer: "))
second = int(input("Enter second integer: "))
third = int(input("Enter third integer: "))
numbers = [first, second, third]
minimum = min(numbers)
maximum = max(numbers)
middle = (first + second + third) - (minimum + maximum)
print(minimum, middle, maximum)
