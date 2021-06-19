class Warehouse:

	def __init__(self, printers = 0, xeroxes = 0, scanners = 0):

		self.database = {'Printer': printers, 'Xerox': xeroxes, 'Scanner': scanners}
		self.full_database = {'Printer': [], 'Xerox': [], 'Scanner': []}

	def receive(self, *goods):
		for j in goods:
			self.database[type(j).__name__] += 1
			self.full_database[type(j).__name__].append(j)

	def shipping(self, *goods):
		for j in goods:
			for elem in self.full_database[type(j).__name__]:
				if j.name == elem.name:
					print(f'successfully shipped {elem.name}')
					self.full_database[type(j).__name__].remove(elem)
					self.database[type(j).__name__] -= 1


class OfficeEquipment:

	def __init__(self, name = '', price = 0, weight = 0):
		
		self.name = name
		try:
			self.price = float(price)
		except ValueError:
			print(f'{type(self).__name__} {self.name}: incorrect price input: set default price = 0')
			self.price = 0
		try:
			self.weight = float(weight)
		except ValueError:
			print(f'{type(self).__name__} {self.name} incorrect weight input: set default weight = 0')
			self.weight = 0



	def setprice(self, price):
		self.price = price

	def setname(self, name):
		self.name = name

	def setweight(self, weight):
		self.weight = weight

class Printer(OfficeEquipment):
	
	def __init__(self, name = '', price = 0, weight = 0, colours = 256*256*256):
		super().__init__(name, price, weight)
		self.colours = colours

class Xerox(OfficeEquipment):
	def __init__(self, name = '', price = 0, weight = 0, paper = 'A4'):
		super().__init__(name, price, weight)
		self.paper = paper

class Scanner(OfficeEquipment):
	def __init__(self, name = '', price = 0, weight = 0, resolution = 200):
		super().__init__(name, price, weight)
		self.resolution = resolution


mistake = Xerox('adssa', 'sadas', 'saasda')
print(mistake.price)
printers = Printer('Brother DCP 1510r', price = 8000, weight = 5), Printer('Brother DCP 1512r', price = 9000, weight = 5)
xeroxes = Xerox('Genius', price = 4000, weight = 4.8)
scanners = Scanner('Genius Scanner', price = 2000, weight = 2.5)

varshavka = Warehouse()

varshavka.receive(*printers, xeroxes, scanners)
print(varshavka.database)
varshavka.shipping(*printers)
print(varshavka.database)

# print(varshavka.database)
# print(list(map(lambda x : x.name, varshavka.full_database['Printer'])))
# print(varshavka.items)
