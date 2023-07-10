import sys
def safe_print_integer_err(value):
	try:
		print("{:d}".format(value))
		return True
	except ValueError as verr:
		print(f"Exception",end="")
		sys.stderr.write(str(verr))
	return False
