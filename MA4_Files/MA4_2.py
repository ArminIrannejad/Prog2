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
	x = [i for i in range(20, 31)]
	pyy = []
	numby = []
	cppy = []

	#for i in x:

		#start = pc()
		#fib_py(i)
		#end = pc()
		#time = round(end-start, 3)
		#pyy.append(time)
		#print(f'Normal Python took {round(end-start, 2)} seconds')


	for i in x:
		start = pc()
		fib_numb(i)
		end = pc()
		time = round(end-start, 4)
		numby.append(time)
		print(f'Python but with numba took {time} seconds')
	for i in x:

		f = Person(i)
		start = pc()
		f.Fib()
		end = pc()
		time = round(end-start, 3)
		cppy.append(time)
		print(f'Python called and compiled in C++ took {round(end-start,2)} seconds')		#47 gives negative number, guess it goes over some kind of maximum range for C++;


	fig = plt.figure()
	ax = fig.add_subplot()
	#ax.scatter(x, pyy, c = 'red', label='Python')
	ax.scatter(x, numby, c='blue', label='Numba')
	ax.scatter(x, cppy, c='green', label = 'C++')
	plt.xlabel('n')
	plt.ylabel('time(s)')
	plt.legend(loc='upper left')
	plt.title('Numba vs C++')
	plt.show()
	plt.savefig('Time N and C++')
if __name__ == '__main__':
	main()
