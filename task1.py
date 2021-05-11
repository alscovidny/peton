duration_seconds = 400153

if not duration_seconds // 60:
	seconds = duration_seconds
	print('seconds: ',seconds)

else:
	minutes = duration_seconds // 60
	seconds = duration_seconds % 60
	if not minutes // 60:
		print(f'{minutes} мин {seconds} сек')
	else:
		hours = minutes // 60
		minutes = minutes % 60
		if not hours // 24:
			print(f'{hours} час {minutes} мин {seconds} сек')
		else:
			days = hours // 24
			hours = hours % 24
			print(f'{days} дн {hours} час {minutes} мин {seconds} сек')

#ниже закоменчена тестировочная версия программы

'''
duration_list = [53, 153, 4153, 400153]

for duration in duration_list:
	print(f'current duration is {duration} seconds')
	if not duration // 60:
		seconds = duration
		print('seconds: ',seconds)

	else:
		minutes = duration // 60
		seconds = duration % 60
		if not minutes // 60:
			print(f'{minutes} мин {seconds} сек')
		else:
			hours = minutes // 60
			minutes = minutes % 60
			if not hours // 24:
				print(f'{hours} час {minutes} мин {seconds} сек')
			else:
				days = hours // 24
				hours = hours % 24
				print(f'{days} дн {hours} час {minutes} мин {seconds} сек')

'''