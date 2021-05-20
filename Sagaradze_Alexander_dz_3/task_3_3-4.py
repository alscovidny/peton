from collections import OrderedDict

def thesarus_adv(*args):
	
	thesarus = {}

	def make_thesarus(key,value,thesarus):
		if key not in thesarus.keys():
		 	thesarus.setdefault(key, [value])
		
		else:
			update = thesarus[key]
			update.append(value)
			thesarus.update({key : update})		

	for elem in args:
		surname_symbol = [elem[j+1] for j in range(len(elem)) if elem[j] == ' ']
		make_thesarus(surname_symbol[0], elem, thesarus)

	for key,values in thesarus.items():
		lower_thesarus = {}

		for name in values:
			make_thesarus(name[0], name, lower_thesarus)

		print(lower_thesarus)
		# thesarus.update( { key : OrderedDict(sorted(lower_thesarus.items())) } )
		thesarus.update({key : lower_thesarus})

	#print(OrderedDict(sorted(thesarus.items())))
	print(thesarus)

test_list = "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "John Cena"

thesarus_adv(*test_list)

