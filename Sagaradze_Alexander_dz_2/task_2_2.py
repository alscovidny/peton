content_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx,elem in enumerate(content_list):
	'''для поиска чисел внутри элемента лучше всего было бы использовать ф-цию isdigit().
	Иначе можно заморочиться с разделением строки на подстроки, напр, через elem.split(' ') 
	и проводить дальнейшие действия из моего кода для подстрок new_elem.

	'''
	if ord(elem[0]) >= 48 and ord(elem[0]) <= 57:
		content_list.insert(idx + 1, '"')
		content_list.insert(idx + 1, '"')

	elif elem[0] == "+" or elem[0] == "-" and len(elem) > 1:
		if ord(elem[1]) >= 48 and ord(elem[1]) <= 57:
			content_list.insert(idx + 1, '"')
			content_list.insert(idx + 1, '"')

for idx,elem in enumerate(content_list):
	if elem == '"' and content_list[idx+1] == '"':

		content_list[idx] = content_list[idx-1]
		content_list[idx-1] = elem

print(content_list)

#content_list[1] = content_list.['"',elem,'"'] 

'''
	string_number = ''
		if symbol == '+':
			string_number += symbol
		
		elif symbol == '-' or ord(symbol) >= 48 and ord(symbol) <= 57:
			string_number += symbol

'''

	#print(string_number)
'''or not ord(elem[0]) >= 48 and not ord(elem[0]) <= 57'''
