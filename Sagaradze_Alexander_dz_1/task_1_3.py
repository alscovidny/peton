'''No input here. Just testing every element of the range(0,21) which is exactly the set {0, 1, 2, 3, ... , 19, 20}'''

for percent_value in range(0, 21):

	if percent_value == 1:
		print(f'{percent_value} процент')
	elif percent_value >= 2 and percent_value <= 4:
		print(f'{percent_value} процента')
	else:
		print(f'{percent_value} процентов')