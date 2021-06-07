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

calc_cube(2, 3, 4, 5)

# def simple_cache(func):
#    cache = {}

#    def wrapper(*args):
#        # nonlocal cache
#        key = str(*args)
#        if key not in cache:
#            cache[key] = func(*args)
#        return cache[key]

#    return wrapper


# @simple_cache
# def render_input(field):
#    print(f"call render_input('{field}')")
#    return f'<input id="id_{field}" type="text" name="{field}">'

# username_f = render_input('username')
# password_f = render_input('password')
# username_f_2 = render_input('username')
# print(username_f)
# print(password_f)
# print(username_f_2)