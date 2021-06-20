class Complex:

	def __init__(self, real = 0, imaginary = 0):
		self.real = real
		self.imaginary = imaginary

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
		return Complex.__mul__(self, Complex.inverse(other))

	def __itruediv__(self, other):
		return Complex.__mul__(self, Complex.inverse(other))

	def __rtruediv__(self, other):
		return Complex.__mul__(self, Complex.inverse(other))

a = Complex(1,2)
b = Complex(2,1)

c = Complex(real = 1)
d = Complex(imaginary = 1)

print(c.real, c.imaginary)
print(d.real, d.imaginary)

c /= d

print(c.real, c.imaginary)

a *= b

print(a.imaginary)