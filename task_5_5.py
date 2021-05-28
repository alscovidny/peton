from time import perf_counter
from sys import getsizeof
import random

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def generate_longer_list(N):
	
	longer_list = []
	for j in range(N):
		longer_list.append(random.randint(1,10000))

	return longer_list

# src = generate_longer_list(10000)

def simple_filter():
	unrepeatable_list = []
	for elem in src:
		if src.count(elem) == 1:
			unrepeatable_list.append(elem)

	return unrepeatable_list

def clever_filter():
	return (filter(lambda x : src.count(x) == 1, src))

def clever_list_filter():
	return list(filter(lambda x : src.count(x) == 1, src))

print(type(clever_filter()))

def memory_performance_test(function):
	start = perf_counter()
	solution = function
	print(f'Execution time: {perf_counter() - start}')
	print(f'Execution memory: {getsizeof(solution)} bytes')

print('clever_filter')

memory_performance_test(clever_filter())

print('simple_filter')

memory_performance_test(simple_filter())

