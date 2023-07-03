#!/usr/bin/python3

print([i * i for i in range(10) if (i % 2 == 0)])

condition = True
x = 1 if condition else 0

num1 = 100_000_000_000
num2 = 1_000_000_000
total = num1 + num2
print(f'{total:,}')
