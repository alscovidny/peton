import os

current_directory = os.getcwd()

daughter_directories = ['settings', 'mainapp', 'adminapp', 'authapp']

try:
	for directory in daughter_directories:
		os.makedirs(current_directory + r'\my_project\{}'.format(directory))

except FileExistsError:
	print('Данные папки уже существуют.')
