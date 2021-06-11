class Road():

	thickness_cm = 5
	specific_asph_amount_kg = 25 

	def __init__(self):
		self._length = 0
		self._width = 0


	def amount_of_asphalt(self):
		return self._length * self._width * Road.thickness_cm * Road.specific_asph_amount_kg / 1000


varshavka_testing = Road() 
varshavka_testing._length = 5000
varshavka_testing._width = 20

print(varshavka_testing.amount_of_asphalt(), '\n')

mkad = Road()
mkad._length = 108900
mkad._width = 40

print(f'For mkad is needed {mkad.amount_of_asphalt()} kg of asphalt')
