from time import perf_counter

with open("nginx_logs.txt",encoding = 'utf-8') as f:
	start = perf_counter()
	for line in f:
		
		list_a = line.split()

		print(list_a[0],list_a[5][1:],list_a[6])

		del list_a

		break
	print(perf_counter() - start)
	
# print(j)

# with open("nginx_logs.txt",encoding = 'utf-8') as f:
# 	start = perf_counter()
# 	for line in f:
		
# 		a = line.find(' - - ')
# 		print(line[:a])


# 		b = line.find('"', a)
# 		b1 = line.find(' /', b)
# 		print(line[b + 1 : b1])

# 		c = line.find(' HTTP', b1)
# 		print(line[b1 + 2 : c])
# 		# print(list_a[0],list_a[5][1:],list_a[6])

# 		# del list_a

# 		break
# 	print(perf_counter() - start)