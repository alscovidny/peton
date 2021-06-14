class Cell:

	def __init__(self, number_cells = 0):
		self.number_cells = number_cells


	def __add__(self, other):
		return Cell(self.number_cells + other.number_cells)


	def __iadd__(self, other):
		return Cell(self.number_cells + other.number_cells)


	def __sub__(self, other):
		if self.number_cells > other.number_cells:
			return Cell(self.number_cells - other.number_cells)
		else:
			raise ValueError(f'{self.number_cells} < {other.number_cells}')


	def __isub__(self, other):
		if self.number_cells > other.number_cells:
			return Cell(self.number_cells - other.number_cells)
		else:
			raise ValueError(f'{self.number_cells} < {other.number_cells}')


	def __mul__(self, other):
		return Cell(self.number_cells * other.number_cells)


	def __rmul__(self, other):
		return Cell(self.number_cells * other.number_cells)


	def __truediv__(self, other):
		return Cell(self.number_cells // other.number_cells)


	def __floordiv__(self, other):
		return Cell(self.number_cells // other.number_cells)


	def __rtruediv__(self, other):
		return Cell(self.number_cells // other.number_cells)


	def __rfloordiv__(self, other):
		return Cell(self.number_cells // other.number_cells)


	def make_order(self, order = 5):
		cells_str = ''
		for j in range(self.number_cells):
			cells_str += '*'
			if not (j + 1) % order and (j + 1) != self.number_cells:
				cells_str += '\n'
		return cells_str


infusoria = Cell(120)

print(infusoria.make_order(15))

covid_19 = Cell(100)

covid_20 = Cell(150)

covid = covid_20/covid_19

print(covid.number_cells)

covid *= covid_20

covid_20 -= covid_19

print(covid.number_cells)

covid //= covid_20

print(covid.number_cells)

print((covid_19 / covid_20).number_cells)
