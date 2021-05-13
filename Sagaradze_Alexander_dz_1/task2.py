odd_numbers_cube = []

for number in range(1,1000):
	if number % 2:
		odd_numbers_cube.append(number ** 3)

total_sum_1 = 0

for element in odd_numbers_cube:
	sum_digits = 0
	test_value = element

	while True:
		sum_digits += test_value % 10
		if not test_value // 10:
			break
		test_value = test_value // 10
	if not sum_digits % 7:
		total_sum_1 += element

print('Ответ на задание a: ', total_sum_1)

for index, value in enumerate(odd_numbers_cube):
	odd_numbers_cube[index] += 17

total_sum_2 = 0

for element in odd_numbers_cube:
	sum_digits = 0
	test_value = element

	while True:
		sum_digits += test_value % 10
		if not test_value // 10:
			break
		test_value = test_value // 10
	if not sum_digits % 7:
		total_sum_2 += element

print('Ответ на задание б: ', total_sum_2)