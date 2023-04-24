#!/usr/bin/python
def list_division(my_list_1, my_list_2, list_length):
	num = 0
	result = []

	for i in range(list_length):
		try:
			num = my_list_1[i] / my_list_2[i]
			result.append(num)
		except TypeError:
			result.append(0)
			print("wrong type")
		except ZeroDivisionError:
			result.append(0)
			print('division by 0')
		except IndexError:
			result.append(0)
			print('out of range')
	return result
