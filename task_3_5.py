from random import shuffle, choice

def getjokes(number_jokes, unique_jokes = False):
	"""
	return 
	"""
	
	nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
	adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
	adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

	def make_a_joke():
		joke = (
			choice(nouns), choice(adverbs), choice(adjectives)
			)
		print(' '.join(joke))

	def make_unique_jokes():

		shuffle(nouns)
		shuffle(adverbs)
		shuffle(adjectives)

		joke_database = list(map(lambda x: ' '.join(x), zip(nouns,adverbs,adjectives)))

		if int(number_jokes) >= max(len(nouns), len(adverbs), len(adjectives)):
			print('выведено макисмально возможное количество шуток:')
			print(joke_database)

		elif int(number_jokes) > 0:
			print(joke_database[:number_jokes])

	if str(number_jokes).isdigit():
		print(True)

	make_unique_jokes()

	# else:
	# 	print('введено некорректное количество шуток')



getjokes(9)
