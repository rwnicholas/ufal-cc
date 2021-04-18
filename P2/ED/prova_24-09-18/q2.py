#!/usr/bin/python3

A = [[1, 2, 3],
	 [4, 5, 6]]

B = [[1, 2, 3],
	 [4, 5, 6]]

def maior_elemento_matriz(matrizUnica):
	maior = matrizUnica[0][0]

	for lista in matrizUnica:
		for x in lista:
			if x > maior:
				maior = x

	return maior

def soma_matriz(matriz1, matriz2):

 	matrizFinal = []

 	for l in range(len(matriz1)):
 		listaTemp = []
 		for i in range(len(matriz1[0])):
 			soma = matriz1[l][i] + matriz2[l][i]
 			listaTemp.append(soma)
 		matrizFinal.append(listaTemp)

 	print("Maior elemento da Matriz Resultante: %d" %(maior_elemento_matriz(matrizFinal)))
 	return matrizFinal



print("Matriz resultante:", soma_matriz(A, B))

