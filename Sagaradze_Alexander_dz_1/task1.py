'''if only I knew about 'try' and 'except' operators...
I'd use them to catch 'ValueError' when you enter unexpected chars.
But I can't do it, so input only nums, please'''

duration_seconds = int(input("duration = "))

if not duration_seconds // 60:
	seconds = duration_seconds
	print(f'{seconds} сек')

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