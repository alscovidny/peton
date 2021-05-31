import sys
import json

flag = False

def hobby_more_than_users(flag):
	if flag:
		sys.exit(1)

with open("users_hobby.txt",'w', encoding = 'utf-8') as output:

	users = open('users2.csv','r', encoding = 'utf-8')
	hobbies = open('hobby.csv','r', encoding = 'utf-8')
		
	database = {}

	hobby_gen = (line.strip().split(',') for line in hobbies)
	users_gen = (' '.join(line.strip().split(',')) for line in users)

	while True:

		try:
			hobby = next(hobby_gen)
		except StopIteration:
			hobby = None

		try:
			user = next(users_gen)
		except StopIteration:

			try:
				next(hobby_gen)
				flag = True
			except StopIteration:
				pass
			break

		database[user] = hobby
	
	users.close()
	hobbies.close()	
	
	json.dump(database, output, ensure_ascii = False, indent = 4)
	hobby_more_than_users(flag)
