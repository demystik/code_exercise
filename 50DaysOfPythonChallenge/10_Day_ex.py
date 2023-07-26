#!/usr/bin/python3
def convert_numbers(my_list):
    num = [f'{i:,}' for i in my_list]
    print(num)


arg = [1000000, 2356989, 2354672, 9878098]
convert_numbers(arg)

