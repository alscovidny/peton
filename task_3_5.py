from random import shuffle, choice

def get_jokes(number_jokes,
			 unique_jokes = False):
	"""
	Function get_jokes prints the list jokes made from inner lists
	nouns, adverbs and adjectives.

	Keyword arguments:
	number_jokes -- number of jokes desired
	unique_jokes -- True if unique jokes are needed,
	False otherwise (default False)
	"""
	if type(number_jokes) == int and number_jokes > 0:

		nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
		adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
		adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

		def make_a_joke():
			joke = (choice(nouns), choice(adverbs), choice(adjectives))
			return ' '.join(joke)

		def make_jokes():
			return list(map(lambda x: make_a_joke(), range(number_jokes)))

		def make_unique_jokes():
			
			if number_jokes > max(len(nouns), len(adverbs), len(adjectives)):
				print(f'выведено максимально возможное количество шуток: {max(len(nouns), len(adverbs), len(adjectives))}')
		
			shuffle(nouns)
			shuffle(adverbs)
			shuffle(adjectives)

			return list(map(lambda x: ' '.join(x), zip(nouns,adverbs,adjectives)))

		if unique_jokes:
			joke_database = make_unique_jokes()[:number_jokes]
			
		else:
			joke_database = make_jokes()

		print(joke_database)

	else:
		print('Ошибка выполнения функции getjokes. Введите целое число > 0')


help(get_jokes)

joke_number = input('Введите желаемое число шуток: ')

if joke_number.isdigit() and int(joke_number) > 0:
	joke_number = int(joke_number)

get_jokes(joke_number)
