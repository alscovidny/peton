price_list = [ 
	71.67, 62.04, 50.06, 10.54, 83.19, 40.03, 75.75, 97.79, 15.40, 76.54,
	16.03, 44.56, 21.60, 25.00, 90.23, 19.93, 58.48, 55.82, 70.45, 31.54
	]

#A. Вывод всех чисел через запятую
price_string_list = []

for i in range(len(price_list)):
	
	roubles = int(price_list[i] // 1)
	kopeks = int((price_list[i] - roubles) * 100) 
	price_string_list.append('{roubles:d} руб {kopeks:02d} коп'.format(roubles = roubles, kopeks = kopeks))

#для читаемости результата разделено на запятую с пробелом
print(', '.join(price_string_list))

#B. Вывод списка по возрастанию. Новый список не был создан.

print(f'индекс исходн. списка: {id(price_list)}')

price_list.sort()

print(f'индекс отсорт. списка: {id(price_list)}')
print(f'отсортированный по возрастанию список: \n{price_list}')

#C. Список, отсортированный по убыванию

#срез создаёт новый список (проверил по индексам объектов в процессе выполнения работы).
decreasing_prices = price_list[::-1]

# в пункте C не предусмотрен вывод. но для вывода достаточно раскоментить строку ниже:
# print(decreasing_prices)

#D. Пять самых дорогих товаров: 
print('цена 5-ти самых дорогих товаров: ')
for price in decreasing_prices[:5]:
	print(price)

# Либо просто print(decreasing_prices[:5]), но выведет объект список



