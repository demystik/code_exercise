#!/usr/bin/python3
def zeros_last(Mylist):
    Mylist.sort()
    num = [Mylist.pop(index) for index, i in enumerate(Mylist) if i == 0]
    Mylist += num
    return Mylist
#print(zeros_last([1, 4, 6, 0, 7,0,9]))
print(zeros_last([2, 1, 4, 7, 6]))
