class Car():

	def __init__(self, speed = 0, color = '', name = '', is_police = False):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police


	def show_speed(self):
		print(f'{self.name} speed is {self.speed}')


	def go(self):
		print(f'{self.name} go')


	def stop(self):
		print(f'{self.name} stopped')


	def turn(self, direction):
		if direction == 'left':
			print(f'{self.name} turned left')
		elif direction == 'right':
			print(f'{self.name} turned right')


class TownCar(Car):

	def show_speed(self):
		if self.speed > 60:
			print(f'speed limit exceeded: {self.name} speed is {self.speed}')
		else:
			print(f'{self.name} speed is {self.speed}')


class WorkCar(Car):

	def show_speed(self):
		if self.speed > 40:
			print(f'speed limit exceeded: {self.name} speed is {self.speed}')
		else:
			print(f'{self.name} speed is {self.speed}')


class SportCar(Car):
	pass

class PoliceCar(Car):

	def __init__(self, speed = 0, color = '', name = ''):
		super().__init__(speed = 0, color = '', name = '')
		self.is_police = True
