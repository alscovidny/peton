import sys
from itertools import islice

stream = list(sys.argv[1:])

if not stream:
	with open('bakery.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			print(line.strip())

if stream:
	with open('bakery.csv', 'r', encoding = 'utf-8') as f:
		if len(stream) == 1:
			skiplines = islice(f, int(stream[0]) - 1, None)
			for line in skiplines:
				print(line.strip())
		else:
			skiplines = islice(f, int(stream[0]) - 1, int(stream[1]))
			for line in skiplines:
				print(line.strip())
