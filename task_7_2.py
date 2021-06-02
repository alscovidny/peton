import os



depth = 0
string_dir = os.getcwd()

with open('config.yaml','r', encoding = 'utf-8-sig') as f:

	for line in f:

		if depth == 0:
			string_dir += r'\{}'.format(line.strip())
			depth += 1
			os.makedirs(string_dir)
			print(string_dir)

		elif depth <= line.count('    '):
			depth = line.count('    ')

			if line.strip().endswith('.py') or line.strip().endswith('.html'):
				
				print(string_dir)
				os.chdir(string_dir)
				print('текущая директория: ', os.getcwd())
				print(line.strip())
				f = open(line.strip(), 'x', encoding = 'utf-8')
				f.close()
			
			else:

				string_dir = string_dir + r'\{}'.format(line.strip())
				os.makedirs(string_dir)
				print(string_dir)

		elif depth > line.count('    '):

			kick_dirs = depth - line.count('    ')
			depth = line.count('    ')
			for _ in range(kick_dirs):
				string_dir = string_dir[ : string_dir.rfind("\\") ]
			
			string_dir += r'\{}'.format(line.strip())
			os.makedirs(string_dir)
			print(string_dir)
