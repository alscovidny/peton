import sys
from itertools import islice

stream = list(map(str,sys.argv[1:]))

with open('bakery.csv', 'r+', encoding = 'utf-8') as f:

	j = 0
	while j < int(stream[0]) - 1:
		j += 1
		f.readline().strip('\n')

	current_position = f.tell()
	found_position = current_position
	f.readline().strip('\n')
	last_correcting_symblol = f.tell()

	if current_position == last_correcting_symblol:
		print('запись не найдена')
		sys.exit(0)

	f.seek(current_position)

	while f.tell() != last_correcting_symblol:
		f.write(' ')
		found_position = found_position + 1
		f.seek(found_position)

	f.seek(current_position)
	f.write(stream[1] + '\n')
