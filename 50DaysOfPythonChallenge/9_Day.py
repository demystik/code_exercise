#!/usr/bin/python3
def biggest_old(num):
    num =  [i for i in num if(int(i) % 2 == 1)]
    num.sort()
    print(num[-1])

biggest_old("234679")
