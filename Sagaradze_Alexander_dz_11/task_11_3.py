import re

class NotNumberError(Exception):
	def __init__(self, txt = ''):
		self.txt = txt

def only_numbers():
	numbers = []
	flag = True
	while flag:
		for elem in input().split():
			if elem == 'stop':
				flag = False
				break
			try:
				if re.search(r'([+-]?\d+(?:\.\d+)?)', elem):
					numbers.append(float(elem) if '.' in elem else int(elem))
				else:
					raise NotNumberError ('mistake')
			except NotNumberError:
				print(f'{elem} не является числом, в список не добавлено')
	return numbers

print(only_numbers())
		