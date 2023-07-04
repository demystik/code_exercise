#!/usr/bin/python3

def longest_value(dic):
    """function called longest_value that takes a dictionary
    as an argument and returns the first longest value of the
    dictionary
    """

    diction = [ val for val in dic.values()]
    diction.sort(reverse=True)
    print(diction[0])



fruits = {'fruit': 'apple', 'color': 'green'}
longest_value(fruits)
