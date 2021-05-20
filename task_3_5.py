from random import shuffle

def getjokes(number_jokes):

	nouns = [
		'костюм', 'гимнаст', 'аргумент', 'дед',
		'бумер', 'секс', 'жонглёр', 'кузовок'
		]

	adverbs = [
		'НЕ ОЧЕНЬ', 'быстро', 'Т О К С И Ч Н О', 'высоко',
		'смутно', 'однозначно', 'никогда', 'послезавтра'
		]

	adjectives = [
		'чёрный', 'мягкий', 'столетний', 'опоздавший',
		'модный', 'многообещающий', 'прошедший', 'неподъёмный'
		]

	shuffle(nouns)
	shuffle(adverbs)
	shuffle(adjectives)

	if str(number_jokes).isdigit():

		number_jokes = int(number_jokes)
		joke_database = list(map(lambda x: ' '.join(x), zip(nouns,adverbs,adjectives)))

		if number_jokes >= max(len(nouns), len(adverbs), len(adjectives)):
			
			print('выведено макисмально возможное количество шуток:')
			print(joke_database)
		elif number_jokes > 0:
			print(joke_database[:number_jokes])

	else:
		print('введено некорректное количество шуток')


a = input()

getjokes(9)
