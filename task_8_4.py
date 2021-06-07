from functools import wraps
from sys import argv
from decimal import Decimal

argument = int(str(*argv[1:2])) if '.' not in str(*argv[1:2]) else Decimal(str(*argv[1:2]))

def val_checker(x = 0):

	def inner_val_checker(function):
		@wraps(function)
		def wrapper(args):
			if args <= 0:
				raise ValueError (f'wrong val {args}')
			else:
				return function(args)

		return wrapper

	return inner_val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

print(calc_cube(argument))
