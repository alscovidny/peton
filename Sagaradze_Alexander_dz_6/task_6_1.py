from collections import Counter

full_data = []
users = []

with open("nginx_logs.txt", encoding = 'utf-8') as f:

	for line in f:
		
		list_a = line.split()

		single_tuple = list_a[0], list_a[5][1:], list_a[6]
		users.append(list_a[0])

		del list_a
		full_data.append(single_tuple)

	cnt = Counter(users)
	spamer = cnt.most_common(1)

	spamer_ip, requests_number = spamer[0]
	print(f'Spamer detected: ip {spamer_ip}\nRequests number: {requests_number}')
