#!/usr/bin/python3
def is_vow(inp):
    vowels = ['a','i','e','o','u']
    for i in range(len(inp)):
        for lett in vowels:
            if inp[i] == ord(lett):
            	inp[i] = lett
    return(inp)

inp = [100,100,116,105,117,121]
print(is_vow(inp))
