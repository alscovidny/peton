import re

class Complex:

	def __init__(self, string = '0+0i'):
		if string.split == 'i':
			self.imaginary = 1
		else:
			parse = re.compile(r'(?P<real>[+-]? ?\d+(?:\.\d+)?^i)? ?((?P<imaginary>[+-]? ?\d+(?:\.\d+)?)i)?')
			try:
				self.real = float(re.search(parse, string).group('real').replace(' ', ''))
			except AttributeError:
				self.real = 0
			try:
				self.imaginary = float(re.search(parse, string).group('imaginary').replace(' ', ''))
			except AttributeError:
				self.imaginary = 0


	def __add__(self, other):
		self.real = self.real + other.real
		self.imaginary = self.imaginary + other.imaginary
		return self 

	def __radd__(self, other):
		return Complex.__add__(self, other)

	def __iadd__(self, other):
		return Complex.__add__(self, other)

	def __mul__(self, other):
		new_real = self.real * other.real - self.imaginary * other.imaginary
		new_imaginary = self.imaginary * other.real + self.real * other.imaginary
		self.real = new_real
		self.imaginary = new_imaginary
		return self

	def __rmul__(self, other):
		return Complex.__mul__(self, other)

	def __imul__(self, other):
		return Complex.__mul__(self, other)

	def inverse(self):
		new_real = self.real / (self.real ** 2 + self.imaginary ** 2)
		new_imaginary = - self.imaginary / (self.real ** 2 + self.imaginary ** 2)
		self.real = new_real
		self.imaginary = new_imaginary
		return self

	def __truediv__(self, other):
		return __mul__(self, inverse(other))

a = Complex('1+2i')
b = Complex('2+1i')

c = Complex('1')
d = Complex('  i  ')

print(c.real, c.imaginary)
print(d.real, d.imaginary)

a *= b

print(a.imaginary)