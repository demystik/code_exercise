#!/usr/bin/python3

def odd_even(MyList):
    MyList.sort()
    for i in MyList:
        if i % 2 == 1:
            odd = i
            break
    MyList.reverse()
    for i in MyList:
        if i % 2 == 0:
            even = i
            break
    print(f"{even} - {odd} = {even - odd}")


#odd_even([2,1,3,4,8,6,5,9,7])
odd_even([1,2,4,6])
