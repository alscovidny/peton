import sys

income = str(*sys.argv[1:2])

with open('bakery.csv', 'a+', encoding = 'utf-8') as f:
	f.write(income.strip() + '\n')
