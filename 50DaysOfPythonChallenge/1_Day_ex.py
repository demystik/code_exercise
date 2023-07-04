#!/usr/bin/python3

def longest_value(dic):
    diction = [ val for val in dic.values()]
    diction.sort(reverse=True)
    print(diction[0])

fruits = {'fruit': 'apple', 'color': 'green'}
longest_value(fruits)
