import os
import shutil

directory = os.getcwd()

for dirpath, dirnames, filenames in os.walk(os.path.join(directory, 'my_project')):
	if filenames:
		for file in filenames:
			if file.endswith('.html'):
				new_path = os.path.join(directory, 'my_project', 'templates', dirpath[dirpath.rfind('\\') + 1 :])
				shutil.move(dirpath, new_path)
				break

for dirpath, dirnames, filenames in os.walk(os.path.join(directory, 'my_project')):
	if not filenames and not dirnames:
		os.rmdir(dirpath)
