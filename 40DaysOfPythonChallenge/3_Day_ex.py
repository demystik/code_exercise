#!/usr/bin/python3
def check_lower(names):
    """You are given a list of names above. This list is made up of names
    of lowercase and uppercase letters. Your task is to write a code
    that will return a tuple of all the names in the list that have only
    lowercase letters.
    """
    names.sort(reverse=True)
    names = [name for name in names if (name.islower() == True)]
    print(names)


names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]
check_lower(names)
