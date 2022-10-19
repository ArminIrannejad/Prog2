#!/usr/bin/env python3.9

from sys import builtin_module_names
from person import Person
import random
import matplotlib as plt



def MC_PI(n):
	for i in range(n):
		x = random.uniform(-1,1)
		y = random.uniform(-1,1)
	if (x^2+y^2)^0.5 > 1:
		plt.scatter(x, y, c='blue')
		
def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	

if __name__ == '__main__':
	main()