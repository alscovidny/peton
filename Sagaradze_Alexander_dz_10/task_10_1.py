class Matrix:

	def __init__(self, matrix_list):
		self.matrix = [elem for elem in matrix_list]

	def __str__(self):
		f_string = f''

		for row in range(len(self.matrix)):
			for elem in self.matrix[row]:
				f_string += f'{elem} '
			if row < len(self.matrix) - 1:
				f_string += f'\n'
		return f_string

	def __add__(self, obj):		
		return Matrix([ 
			[self.matrix[i][j] + obj.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))
		])

matrix1 = [
	[1, 4, 3, 5],
	[2, 6, 7, 1]
]


matrix2 = [
	[1, 0, 0, 0],
	[0, 1, 0, 0]
]

a = Matrix(matrix1)
b = Matrix(matrix2)

c = a + b

print(a + b)