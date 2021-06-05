import os
import shutil

files_sizes = []
statistics_dict = {}

directory = os.getcwd()

print(directory)

for dirpath, dirnames, filenames in os.walk(directory):

	if filenames:
		os.chdir(dirpath)
		for file in filenames:
			files_sizes.append(os.stat(file).st_size)

def make_dict():

	max_size = max(files_sizes)
	segment_list = []
	divider = 10

	while max_size // divider:
		segment_list.append(divider)
		statistics_dict.setdefault(divider, 0)
		divider = divider * 10

	segment_list.reverse()

	for elem in files_sizes:
		for value in segment_list:
			if elem > value:
				statistics_dict[value] += 1
				break

	del segment_list

make_dict()
print(statistics_dict)
