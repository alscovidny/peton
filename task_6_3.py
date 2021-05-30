import sys
import json

flag = False

def hobby_more_than_users(flag):
	if flag:
		sys.exit(1)

with open("users_hobby.txt",'w', encoding = 'utf-8') as output:

	users = open('users2.csv','r', encoding = 'utf-8')
	hobby = open('hobby.csv','r', encoding = 'utf-8')
		
	database = {}

	hobby_gen = (line.strip().split(',') for line in hobby)

	for line in users:

		try:
			elem = next(hobby_gen)
			database[' '.join(line.strip().split(','))] = elem
		
		except StopIteration:
			database[' '.join(line.strip().split(','))] = None
			if not flag:
				flag = True
	
	users.close()
	hobby.close()	
	
	json.dump(database, output, ensure_ascii = False, indent = 4)
	hobby_more_than_users(flag)
