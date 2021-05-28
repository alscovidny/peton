from time import perf_counter
from sys import getsizeof
from random import randint

def generate_longer_list(N):
	
	longer_list = []

	for j in range(N):
		longer_list.append(randint(1,10000))

	return longer_list

src = generate_longer_list(10000)

def simple_filter():
	unrepeatable_list = []

	for elem in src:
		if src.count(elem) == 1:
			unrepeatable_list.append(elem)

	return unrepeatable_list

def clever_filter():
	return list(filter(lambda x : src.count(x) == 1, src))

def memory_performance_test(function):
	start = perf_counter()
	memory_volume = function
	ariphmetic_time = sum(function)
	print(f'Execution time: {perf_counter() - start}')
	print(f'Execution memory: {getsizeof(memory_volume)} bytes')

print('clever_filter')
memory_performance_test(clever_filter())

print('simple_filter')
memory_performance_test(simple_filter())
