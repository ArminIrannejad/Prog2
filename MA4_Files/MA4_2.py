#!/usr/bin/env python3
from person import Person
import matplotlib.pyplot as plt
from time import perf_counter as pc
from numba import njit

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

@njit
def fib_numb(n):
	if n <= 1:
		return n
	else:
		return (fib_numb(n-1) + fib_numb(n-2))


def main():
	x = [i for i in range(30, 46)]
	pyy = []
	numby = []
	cppy = []

	"""for i in x:

		start = pc()
		fib_py(i)
		end = pc()
		time = round(end-start, 3)
		pyy.append(time)
		print(f'Normal Python took {round(end-start, 2)} seconds')
	for i in x:
		start = pc()
		fib_numb(i)
		end = pc()
		time = round(end-start, 3)
		numby.append(time)
		print(f'Python but with numba took {round(end-start, 2)} seconds')"""
	for i in x:

		f = Person(i)
		start = pc()
		f.Fib()
		end = pc()
		time = round(end-start, 3)
		cppy.append(time)
		print(f'Python called and compiled in C++ took {round(end-start,2)} seconds')				#47 gives negative number, guess it goes over some kind of maximum range for C++;


	plt.scatter(x, cppy)
	plt.xlabel('n')
	plt.ylabel('time(s)')
	plt.title('Time for c++')
	plt.show()
	plt.savefig('Time cpp')
if __name__ == '__main__':
	main()
