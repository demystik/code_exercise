#!/usr/bin/python3
def multiplication_table(size):
    table = [[0 for i in range(size)] for i in range(size)]
    for num in range(size):
        for i in range(size):
            table[num][i] = (i + 1)  * (num + 1)
    print(table)
    return
multiplication_table(3)
