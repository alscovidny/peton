import sys
import json

flag = False

def hobby_more_than_users(flag):
	if flag:
		sys.exit(1)

def users_generator():

	global flag
	for line in users:

		try:
			yield line.strip() + ': ' + next(hobby_gen) + '\n'

		except StopIteration:
			yield line.strip() + ': ' + 'None' + '\n'
			if not flag:
				flag = True

with open("users_hobby_task_6_4.txt",'w', encoding = 'utf-8') as output:

	users = open('users.csv','r', encoding = 'utf-8')
	hobby = open('hobby.csv','r', encoding = 'utf-8')

	hobby_gen = (line.strip('\n') for line in hobby)
	users_gen = users_generator()

	output.writelines(users_gen)

	users.close()
	hobby.close()
