#!/usr/bin/python3
def swap_values(my_list):
    last, first = my_list.pop(), my_list[0]
    my_list[0] = last
    my_list.append(first)
    return my_list


print(swap_values([2, 4, 67, 7]))
