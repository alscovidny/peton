import re

class NotNumberError(Exception):
	pass

class OnlyNumbers():

	@staticmethod
	def is_not_a_number(string):
		for x in ''.join(string.split()):
			if not x.isdigit() and x!='.':
				raise NotNumberError

	@staticmethod
	def find_numbers(string):
		try:
			OnlyNumbers.is_not_a_number(string)
		except NotNumberError:
			print('found chars in input')

		numbers = re.findall(r'(\d+(?:\.\d+)?)', string)
		return list(map(lambda x : float(x) if '.' in x else int(x), numbers))

	def __init__(self):
		self.only_numbers = []
		while 1:
			a = input()
			if 'stop' in a:
				a = a[ : a.rfind('stop')]
				self.only_numbers.extend(OnlyNumbers.find_numbers(a))
				break
			self.only_numbers.extend(OnlyNumbers.find_numbers(a))

	def __str__(self):
		return self.only_numbers

list_numbers = OnlyNumbers()

print(list_numbers.only_numbers)
		