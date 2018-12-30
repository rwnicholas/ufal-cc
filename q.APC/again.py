#!/usr/bin/python3

def multi_matriz(matriz1, matriz2):
	matrizFinal = []

	for l in range(len(matriz1)):
		listaTemp = []
		for c in range(len(matriz2[0])):
			soma = 0
			for i in range(len(matriz1[0])):
				soma += matriz1[l][i] * matriz2[i][c]
			listaTemp.append(soma)
		matrizFinal.append(listaTemp)

	return matrizFinal

matriz1 = [[1, 2, 3], #2x3
		   [4, 5, 6]]
matriz2 = [[1, 2], #3x2
		   [3, 4],
		   [5, 6]]

if len(matriz1[0]) != len(matriz2):
	print("Impossível multiplicar")
else:
	print(multi_matriz(matriz1, matriz2))