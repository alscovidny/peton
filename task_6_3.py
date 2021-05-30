import sys
import json

j = 0

with open("users_hobby.txt",'w', encoding = 'utf-8') as output:

	users = open('users.csv','r', encoding = 'utf-8')
	hobby = open('hobby.csv','r', encoding = 'utf-8')
		
	database = {}
	hobby_list = []

	# for line in hobby:

	# 	hobby_list.append(line.strip().split(','))

	print(len(hobby_list))
	print(hobby_list)

	for line in users:
		print(j)
		if j >= len(hobby_list):
			database[' '.join(line.strip().split(','))] = None
		else:
			database[' '.join(line.strip().split(','))] = hobby_list[j]
		j += 1
	
	users.close()
	hobby.close()	
	
	json.dump(database, output, ensure_ascii = False, indent = 4)

	if j < len(hobby_list):
		sys.exit(1)
