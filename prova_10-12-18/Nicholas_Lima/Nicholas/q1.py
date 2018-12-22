#!/usr/bin/python3

#Não eficiente
def n_eficiente(lista):
	#Insertion Sort
	count1 = 0
	for i in range(1, len(lista)):
		aux = i
		while lista[aux-1] > lista[aux]:
			count1+=1
			lista[aux-1],lista[aux] = lista[aux],lista[aux-1]
			if aux > 1:
				aux-=1
	print("Trocas não eficientes:",count1)
	return lista

#Eficiente
def eficiente(lista):
	#Shell Sort
	count2 = 0
	h = setH(lista)
	while h!=1:
		h = h//3
		for i in range(h, len(lista)):
			aux = i
			while lista[aux-h] > lista[aux]:
				count2+=1
				lista[aux-h],lista[aux] = lista[aux],lista[aux-h]
				aux-=h
				if aux < h:
					break
	return lista
	
def setH(lista):
	h = 1
	while (3*h)+1 < len(lista):
		h = (3*h)+1
	return h

# lista = [8,5,6,3,9,1,8,5,6,3,9,1,2,5]
# lista2 = [8,5,6,3,9,1,8,5,6,3,9,1,2,5]
