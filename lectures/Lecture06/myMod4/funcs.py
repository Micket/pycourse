"""
Additional methods for printing
"""

def print_one(arg1):
	print(arg1)

def print_two(arg1, arg2):
	print(arg1, arg2)

def print_many(*args):
	for i in args[:-1]:
		print(i, end=': ')
	print(args[-1])

