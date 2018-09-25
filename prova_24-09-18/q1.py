#!/usr/bin/python3
A = [1,5,3,4,7,8]
B = [6,10,9,11]

#A = [5, 2, 3, 6, 4]
#B = [8, 9, 11, 12, 10]

def retornarConj(a, b):
	minA = a[0]
	maxA = a[0]

	minB = b[0]
	maxB = b[0]

	for x in a:
		if x < minA:
			minA = x
		if x > maxA:
			maxA = x

	for x in b:
		if x < minB:
			minB = x
		if x > maxB:
			maxB = x
	auxA = []
	auxB = []

	for x in range(minA, maxA+1):
		auxA.append(x)

	for x in range(minB, maxB+1):
		auxB.append(x)
	
	status = "NAO"
	for x in range(len(auxA)):
		if x in auxB:
			status = "SIM"

	return status
	



print(retornarConj(A, B))
