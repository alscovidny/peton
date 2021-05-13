#percent_value = int(input("Введите количество процентов от 0 до 20: "))

for percent_value in range(0,21):

#if percent_value >= 0 and percent_value <= 20:

	if percent_value == 1:
		print(f'{percent_value} процент')
	elif percent_value >= 2 and percent_value <= 4:
		print(f'{percent_value} процента')
	else:
		print(f'{percent_value} процентов')