#!/usr/bin/python3
def equal_strings(str_a, str_b):
    if len(str_a) == len(str_b):
        for i in range(len(str_a)):
            if str_a[i] not in str_b:
                return False
        return True


print(equal_strings("love", "evol"))
