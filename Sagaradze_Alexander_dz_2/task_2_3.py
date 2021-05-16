personal_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for elem in personal_data:
	name = elem.split(' ')[-1].capitalize()
	print("Привет, %s!" % (name))



