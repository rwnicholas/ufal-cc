#!/usr/bin/python3

def multiFuncao(matriz1, matriz2):
	matrizFinal = []

	for l in range(len(matriz1)):
		lista = []
		for c in range(len(matriz2[0])):
			soma = 0
			for i in range(len(matriz1[0])):
				soma += matriz1[l][i] * matriz2[i][c]
			lista.append(soma)
		matrizFinal.append(lista)
		
	return matrizFinal

matriz1 = [[1, 2, 3, 4, 5]] #1x5

matriz2 = [[1], #5x1
		   [2],
		   [3],
		   [4],
		   [5]]

if (len(matriz1[0]) != len(matriz2)): #colunas de 1 = linhas de 2
	print("Multiplicação impossível!")
else:
	print(multiFuncao(matriz1, matriz2))