import re

# class Complex:

# 	def __init__(self, string):

parse = re.compile(r'^(?P<real>[+-]? ?\d+(.\d+)?)?(?=[+-])? ?(?P<imaginary>[+-]? ?\d+(.\d+)?i)?$')

b = str('+ 2i')

print(re.search(parse, b).groupdict()['imaginary'])

