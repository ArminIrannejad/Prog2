import random
import matplotlib.pyplot as plt
import math
import functools as ft
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future 

def MC_PI(n):
	utex = []
	utey = []
	innex = []
	inney = []
	for i in range(n):
		x = random.uniform(-1,1)
		y = random.uniform(-1,1)
		if (x**2+y**2)**0.5 > 1:
			utex.append(x)
			utey.append(y)
		else:
			innex.append(x)
			inney.append(y)
	plt.scatter(utex, utey, c='blue')
	plt.scatter(innex, inney, c='red')
	plt.xlim(-1,1)
	plt.xlim(-1,1)
	plt.show()
	return print('Pi enligt mig:', 4*len(innex)/len(innex + utex), f'Punkter innanför cirkeln {len(innex)}. Pi enligt Python {math.pi}')


def MC_HS(n, d):
	ute = 0
	inne = 0
	for i in range(n):
		lista = [random.uniform(-1, 1) for i in range(d)] 
		square = list(map(lambda x: x**2,lista))
		summa = ft.reduce(lambda x,y: x+y, square)
		dist = summa**(1/d)
		if dist > 1:
			ute += 1
		else:
			inne += 1
	return inne/(inne + ute)


def runner(n):
	print(f'Performing costly function {n}')
	pause(n)
	return f'function {n} has completed'
	
def main():
	MC_PI(1000)
	volume1 = math.pi/math.gamma(2)*0.25
	volume2 = math.pi**(11/2)/math.gamma(6.5)* 0.5**11
	print(f'Mitt svar: {MC_HS(100000,2)} facit:{volume1} Mitt svar: {MC_HS(100000,11)} facit: {volume2}')

	nn = 10000000
	nd = 11
	n_proc = 10
	dim = n_proc*[nd]
	dots = [nn//10 for i in range(n_proc)]

	start = pc()
	result = MC_HS(nn, nd)
	end = pc()
	print(f' Process 1 took {round(end-start, 2)} seconds')

	start = pc()
	with future.ProcessPoolExecutor() as ex:
		results = ex.map(MC_HS, dots, dim)
	results = list(results)
	end = pc()
	print(f' Process 2 took {round(end-start, 2)} seconds')
	


if __name__ == '__main__':
	main()


