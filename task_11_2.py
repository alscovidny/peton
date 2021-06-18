class ExceptDivision(Exception):

	def __init__(self, value = 0):
		self.value = value

	def __truediv__(self, divider):
		try:
			return self.value / divider
		except ZeroDivisionError:
			print(f'Can not divide by zero')
			return None

	def __floordiv__(self, divider):
		try:
			return self.value // divider
		except ZeroDivisionError:
			print(f'Can not divide by zero')
			return None

	def __mod__(self, divider):
		try:
			return self.value // divider
		except ZeroDivisionError:
			print(f'Can not divide by zero')
			return None

	def __itruediv__(self, divider):
		return ExceptDivision.__truediv__(self, divider)

	def __ifloordiv__(self, divider):
		return ExceptDivision.__floordiv__(self, divider)

	def __ifloordiv__(self, divider):
		return ExceptDivision.__floordiv__(self, divider)

a = ExceptDivision(-2)
c = 2

a //= c
