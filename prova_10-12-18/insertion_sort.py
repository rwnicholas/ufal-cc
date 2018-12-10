#!/usr/bin/python3

def insertion_sort(lista):
	for i in range(1,len(lista)):
		aux = i
		while (lista[aux-1] > lista[aux]):
			lista[aux-1],lista[aux] = lista[aux],lista[aux-1]
			if aux > 1:
				aux-=1
	return lista


# [7,2,9,4,3,8,6,1]
# [8,4,2,5,3,6]

print(insertion_sort([8,4,2,5,3,6]))