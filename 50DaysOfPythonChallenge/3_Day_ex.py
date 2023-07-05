#!/usr/bin/python3
def check_lower(names):
    names.sort(reverse=True)
    names = [name for name in names if (name.islower() == True)]
    print(names)


names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]
check_lower(names)
