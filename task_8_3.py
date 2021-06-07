from functools import wraps

def type_logger(function):
	@wraps(function)
	def wrapper(*args, **kwargs):
		if args:
			for elem in args:
				print(f'{function.__name__}({elem}: {type(elem)})', end=', ')
			print()
		if kwargs:
			print(f'{function.__name__}({kwargs[str(*kwargs)]}: {type(kwargs[str(*kwargs)])})')
	return wrapper


@type_logger
def calc_cube(x = 1):
	return x ** 3


calc_cube(2.2, 3, 4, 5)
