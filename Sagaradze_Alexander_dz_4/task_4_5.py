from sys import argv
from utils import currency_rates

result = list(map(currency_rates, argv[1:]))

for elem in result:
	print(elem)
