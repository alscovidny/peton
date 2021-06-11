class Worker():

	def __init__(self, _income = {'wage': 0, 'bonus': 0}):
		self.name = ''
		self.surname = ''
		self.position = ''
		self._income = _income


	def set_wage(self, wage):
		self._income['wage'] = int(wage)


	def set_bonus(self, bonus):
		self._income['bonus'] = bonus


class Position(Worker):

	def get_full_name(self):
		return self.name + ' ' + self.surname


	def get_total_income(self):
		return self._income['wage'] + self._income['bonus']


engineer = Position()

engineer.name = 'Boris'
engineer.surname = 'Bespalov'

engineer.position = 'engineer'

engineer.set_wage(25000)
engineer.set_bonus(15000)

print(engineer.get_full_name())
print(engineer.get_total_income())
