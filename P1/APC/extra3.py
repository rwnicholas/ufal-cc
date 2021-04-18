#!/usr/bin/python3

# quad = [[8,3,4],
# 		[1,5,9],
# 		[6,7,2]]

quad = [[1,2,3],
		[4,5,6],
		[7,8,9]]

if len(quad) != len(quad[0]):
	print("Fail")
	exit(0)

def somaColuna(matriz):
	soma = None

	for c in range(len(matriz[0])):
		somaTemp = 0
		for l in range(len(matriz)):
			somaTemp += matriz[l][c]
		if soma == None:
			soma = somaTemp
		elif soma != somaTemp:
			return False

	return soma

def somaLinha(matriz):
	soma = None

	for l in range(len(matriz)):
		somaTemp = 0
		for c in range(len(matriz[0])):
			somaTemp += matriz[l][c]
		if soma == None:
			soma = somaTemp
		elif soma != somaTemp:
			return False

	return soma

def somaDiagonal(matriz):
	soma = 0

	for i in range(len(matriz[0])):
		soma += matriz[i][i]

	return soma

def quadPerfect(matriz):
	
	if somaColuna(matriz) == somaLinha(matriz) and somaColuna(matriz) == somaDiagonal(matriz):
		return True
	return False

print(quadPerfect(quad))