content_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx,elem in enumerate(content_list):

	if ord(elem[0]) >= 48 and ord(elem[0]) <= 57:
		if len(elem) == 1:
			content_list[idx] = '0' + elem[0]
		elif len(elem) == 2:
			content_list[idx] = elem
		'''специфическая реализация. сделано лишь для того, чтобы не создавать еще один список, т.е. выполнить пункт 3'''
		content_list.insert(idx + 1, '"')
		content_list.insert(idx + 1, '"')

	elif elem[0] == "+" or elem[0] == "-" and len(elem) > 1:
		if ord(elem[1]) >= 48 and ord(elem[1]) <= 57:
			if len(elem) == 2:
				content_list[idx] = elem[0] + '0' + elem[1]
			content_list.insert(idx + 1, '"')
			content_list.insert(idx + 1, '"')

for idx,elem in enumerate(content_list):
	if elem == '"' and content_list[idx+1] == '"':
 
		content_list[idx] = content_list[idx-1]
		content_list[idx-1] = elem

print(content_list)

content_string = ''

j = 0

while j <= len(content_list):
	
	if len(content_list) - j > 0:
		if content_list[j] == '"' and content_list[j+2] == '"':
			content_string += content_list[j] + content_list[j+1] + content_list[j+2] + ' '
			j += 2
		else:
			content_string += content_list[j] + ' '
	j += 1

print(content_string)