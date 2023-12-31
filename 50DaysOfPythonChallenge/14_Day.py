#!/usr/bin/python3

def flat_list(myList):
    myList = str(myList)

    myList = myList.replace("[","")
    myList = myList.replace("]","")
    myList = f"[{myList}]"
    myList = list(myList)
    print(type(myList))


myList = [1,2,3,[9, 8, 6, 7], 4,5, [2, 4, 5]]
flat_list(myList);