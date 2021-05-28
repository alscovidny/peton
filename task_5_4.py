from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def economy_result():
	return (src[num] for num in range(1,len(src)) if src[num] > src[num-1])

def fast_result():
	return [src[num] for num in range(1,len(src)) if src[num] > src[num-1]]

def memory_performance_test(function):
	start = perf_counter()
	solution = function
	print(f'Execution time: {perf_counter() - start}')
	print(f'Execution memory: {getsizeof(solution)} bytes')


print(f'function: economy_result')
memory_performance_test(economy_result())

print()

print(f'function: fast_result')
memory_performance_test(fast_result())
