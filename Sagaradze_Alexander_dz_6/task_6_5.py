import sys

users_name, hobby_name, output_name = map(str, sys.argv[1:4])

with open(output_name,'w+', encoding = 'utf-8') as output:

	with open(users_name,'r', encoding = 'utf-8') as users_file:
		with open(hobby_name,'r', encoding = 'utf-8') as hobbies_file:

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
