#!/usr/bin/python3
def get_count(sentence):
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	count = 0
	for i in sentence:
		if i in vowels:
			count += 1
	print(count)
get_count("Hello how are you doing")
