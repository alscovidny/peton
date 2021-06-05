import os
import shutil
import json

files = []
statistics_dict = {}

directory = 'C:\\Users\\Александр\\Desktop\\muzlo'

for dirpath, dirnames, filenames in os.walk(directory):

	if filenames:
		os.chdir(dirpath)
		for file in filenames:
			files.append((os.stat(file).st_size, file[file.rfind('.') + 1 :]))

def make_dict():
	
	max_size = 0
	for file_size, extension in files:
		if file_size > max_size:
			max_size = file_size

	segment_list = []
	divider = 10

	while max_size // divider:
		segment_list.append(divider)
		statistics_dict.setdefault(divider, (0,set()))
		divider = divider * 10

	segment_list.reverse()

	for file_size, extension in files:
		for value in segment_list:
			if file_size > value:
				statistics_dict[value][1].add(extension)
				statistics_dict[value] = statistics_dict[value][0] + 1, statistics_dict[value][1]
				break

	del segment_list
	statistics_dict[value] = statistics_dict[value][0] + 1, list(statistics_dict[value][1])


make_dict()
print(statistics_dict)

# print()
# with open(directory[directory.rfind('\\') + 1 :], 'w', encoding = 'utf-8') as f:
# 	json.dump(statistics_dict,f)
