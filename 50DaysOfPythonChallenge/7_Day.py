#!/usr/bin/python3
def string_range(num):
    string = ""
    for i in range(num):
        string += str(i)
        if i < num - 1:
            string += "."
    return string

print(string_range(6))
