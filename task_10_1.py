class Matrix:

	def __init__(self, matrix_list):
		self.matrix = [elem for elem in matrix_list]

	def __str__(self):

		
		f_string = f''

		for row in self.matrix:
			for elem in row:
				f_string += f'{elem} '
			f_string += f'\n'

		return f_string
				


matrix = [
	[1, 4, 3, 5],
	[2, 6, 7, 1]
]

a = Matrix(matrix)

# print(a.matrix)

print(a)