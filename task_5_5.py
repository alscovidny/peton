src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def clever_filter():
	return list(filter(lambda x : src.count(x) == 1, src))

print(clever_filter())
