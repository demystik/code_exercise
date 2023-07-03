#!/usr/bin/python3

print([i * i for i in range(10) if (i % 2 == 0)])



condition = True
x = 1 if condition else 0



num1 = 100_000_000_000
num2 = 1_000_000_000
total = num1 + num2
print(f'{total:,}')


with open('myFile.txt', 'r') as file:
	fileContent = file.read()
words = fileContent.split(' ')
print(len(words))


colors = ['yellow', 'white', 'red', 'blue', 'green', 'violet', 'indigo', 'black']
for index, color in enumerate(colors, start=1):
	print(index, color)


names = ['Peter parker', 'Clark kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']
