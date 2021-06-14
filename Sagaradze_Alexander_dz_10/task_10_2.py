from abc import ABC, abstractmethod

class Clothes(ABC):

	def __init__(self, name = ''):
		self.name = name

	@abstractmethod
	def cloth_amount(self):
		pass

class Coat(Clothes):

	def __init__(self, name = '', size = 0):
		super().__init__()
		self.size = size

	def size(self, size = 0):
		self.size = size

	@property
	def cloth_amount(self):
		return round(self.size / 6.5 + 0.5, 1)

class Suit(Clothes):

	def __init__(self, name = '', height = 0):
		super().__init__()
		self.height = height

	def height(self, height = 0):
		self.height = height

	@property
	def cloth_amount(self):
		return round(self.height * 2 + 0.3, 1)

coat = Coat('Zolla', 40)
suit = Suit('Peplos', 50)

print(suit.cloth_amount)
print(coat.cloth_amount)
