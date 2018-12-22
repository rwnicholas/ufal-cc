#!/usr/bin/python3

def fibo(m):
	f = 0
	ant = 0
	for i in range(1,m+1):
		if i == 1:
			f = 1
			ant = 0
		else:
			f+=ant
			ant = (f - ant)
	return f

print(fibo(100000000))