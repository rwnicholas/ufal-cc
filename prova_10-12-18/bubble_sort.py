#!/usr/bin/python3

def bubble_sort(lista):
	for i in range(len(lista)-1):
		for j in range(1,len(lista)-i):
			if lista[j-1] > lista[j]:
				lista[j],lista[j-1] = lista[j-1],lista[j]
	return lista


# [7,2,9,4,3,8,6,1]
# [8,4,2,5,3,6]

print(bubble_sort([7,2,9,4,3,8,6,1]))