#!/usr/bin/python3

def verificaElementoEmLista(elemento, lista):
	for valor in lista:
		if (elemento == valor):
			return True
	return False

def conjuntoAemB(a, b):
	for valor in a:
		if verificaElementoEmLista(valor, b) == False:
			return False
	return True

# A = [1,2,3,4,5,6]
# B = [7,8,9,10]

A = [1,2,3,4,5,6]
B = [1,2,3,4,5,6,7,8,9,10]

print(conjuntoAemB(A, B))