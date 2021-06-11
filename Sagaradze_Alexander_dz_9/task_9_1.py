import time

class TrafficLight():

	def __init__(self):
		self.__color = 'red'
		print(self.__color)


	def running(self):
		def switch_light(color):
			self.__color = color
			print(self.__color)


		time.sleep(7)
		switch_light('orange')
		time.sleep(2)
		switch_light('green')
		time.sleep(7)
		print('\nrunning finished')


a = TrafficLight()

a.running()
