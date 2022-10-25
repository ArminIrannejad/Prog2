#!/usr/bin/env python3
from person import Person
import matplotlib as plt
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
	start = pc()
	fib_py(40)
	end = pc()
	print(f'Normal Python took {round(end-start, 2)} seconds')

	start = pc()
	fib_numb(40)
	end = pc()
	print(f'Python but with numba took {round(end-start, 2)} seconds')

	
	f = Person(15)
	start = pc()
	f.Fib()
	end = pc()
	print(f'Python called and compiled in C++ took {round(end-start,2)} seconds')				#47 gives negative number, guess it goes over some kind of maximum range for C++;

	
	

if __name__ == '__main__':
	main()