#!/usr/bin/python3
def array_diff(a, b):
	new_array = []
	for i in a:
		if i not in b:
			new_array.append(i)
	return (new_array)
print(array_diff([1,2],[1]))
