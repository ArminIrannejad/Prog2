#!/usr/bin/env python3
from person import Person
import matplotlib as plt
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

		
def main():
	f = Person(15)
	print(f.Fib())
	
	

if __name__ == '__main__':
	main()