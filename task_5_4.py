from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def economy_result():
	return (src[num] for num in range(1,len(src)) if src[num] > src[num-1])

def fast_access_result():
	return [src[num] for num in range(1,len(src)) if src[num] > src[num-1]]

def memory_performance_test(function):
	start = perf_counter()
	memory_volume = function
	ariphmetic_time = sum(function)
	print(f'Execution time (sum of all the elements): {perf_counter() - start}')
	print(f'Execution memory: {getsizeof(memory_volume)} bytes')

print(f'function: economy_result \n{list(economy_result())} \n')
memory_performance_test(economy_result())

print()

print(f'function: fast_access_result \n{fast_access_result()} \n')
memory_performance_test(fast_access_result())
