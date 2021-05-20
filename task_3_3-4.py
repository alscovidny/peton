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
		
		# if surname_symbol[0] not in thesarus.keys():
		#  	thesarus.setdefault(surname_symbol[0], [elem])
		
		# else:
		# 	update = thesarus[surname_symbol[0]]
		# 	update.append(elem)
		# 	thesarus.update({surname_symbol[0] : update})

	for key,values in thesarus.items():
		lower_thesarus = {}

		for name in values:

			# if name[0] not in lower_thesarus.keys():
			# 	lower_thesarus.setdefault(name[0], [name])
			# else:
			# 	update = lower_thesarus[name[0]]
			# 	update.append(name)
			# 	lower_thesarus.update({name[0] : update})
		print(lower_thesarus)
		thesarus.update({key : lower_thesarus})

	print(thesarus)

test_list = "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"


thesarus_adv(*test_list)

