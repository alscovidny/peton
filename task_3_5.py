from random import shuffle, choice

def getjokes(number_jokes,
			 unique_jokes = False):
	"""
	return 
	"""
	if type(number_jokes) == int and number_jokes > 0:

		nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
		adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
		adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

		def make_a_joke():
			joke = (choice(nouns), choice(adverbs), choice(adjectives))
			return ' '.join(joke)

		def make_unique_jokes():
			
			if number_jokes > max(len(nouns), len(adverbs), len(adjectives)):
				print(f'выведено максимальное количество шуток: {max(len(nouns), len(adverbs), len(adjectives))}')
		
			shuffle(nouns)
			shuffle(adverbs)
			shuffle(adjectives)

			return list(map(lambda x: ' '.join(x), zip(nouns,adverbs,adjectives)))

		if unique_jokes:
			joke_database = make_unique_jokes()
			
		else:
			joke_database = (list(map(lambda x: make_a_joke(), range(number_jokes))))

		print(joke_database)

	else:
		print('Ошибка выполнения функции getjokes. Введите целое число > 0')

getjokes(10,unique_jokes = True)
