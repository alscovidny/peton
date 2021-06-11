class Stationery():

	def __init__(self, title = ''):
		self.title = title


	def draw(self):
		print('Запуск отрисовки')


class Pen(Stationery):

	def draw(self):
		print('Отрисовка ручкой')


class Pencil(Stationery):

	def draw(self):
		print('Отрисовка карандашом')


class Handle(Stationery):

	def draw(self):
		print('Отрисовка маркером')

stat = Stationery()
stat.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()

pen = Pen()
pen.draw()

# pen.draw()



