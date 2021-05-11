#для тестирования программы создадим списочек

#duration_list = [60, 80, 10000, 5009, 543]

duration = 124123

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
