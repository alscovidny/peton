def odd_nums_v2(n):
	return (num for num in range(n+1) if num % 2)

odd_to_13 = odd_nums_v2(13)
print(type(odd_to_13))

print(*odd_to_13)
