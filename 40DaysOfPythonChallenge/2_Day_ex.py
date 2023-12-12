#!/usr/bin/python3
def check_duplicates(list_of_str):
    """
    >>>check_duplicates(['apple', 'orange', 'banana', 'apple'])
    'apple'
    """
    list_of_str.sort()
    for i in range(0, len(list_of_str), 2):
        if list_of_str[i] == list_of_str[i+1]:
            return list_of_str[i]
    return "No Duplicates"

fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(names))
