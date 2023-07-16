#!/usr/bin/python3

def is_square(n):
    if n > 0:
        for i in range(int(n / 2) + 1):
            if i * i == n:
                return True
    return False

print(is_square(144))
