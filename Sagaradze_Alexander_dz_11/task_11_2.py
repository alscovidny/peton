class ExceptDivision(Exception):
	def __init__(self, txt):
		self.txt = txt

b = 0
a = 10

try:
	if b == 0:
		raise ExceptDivision ('dividing by zero')
	print(a/b)
except ExceptDivision: print('can not divide by zero')
