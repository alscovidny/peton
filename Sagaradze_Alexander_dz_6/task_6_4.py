import sys

with open("users_hobby_task_6_4.txt",'w+', encoding = 'utf-8') as output:

	with open('users2.csv','r', encoding = 'utf-8') as users_file:
		with open('hobby.csv','r', encoding = 'utf-8') as hobbies_file:

			for user in users_file:
				output.write(user.strip('\n') + ': ')
				try:
					output.write(next(hobbies_file).strip('\n') + '\n')
				except StopIteration:
					output.write('None' + '\n')
			try:
				next(hobbies_file)
				sys.exit(1)
			except StopIteration:
				pass
