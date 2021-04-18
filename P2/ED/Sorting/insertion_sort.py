#!/usr/bin/python3

def insertion_sort(lista):
	count = 0
	for i in range(1,len(lista)):
		aux = i
		while (lista[aux-1] > lista[aux]):
			count+=1
			lista[aux-1],lista[aux] = lista[aux],lista[aux-1]
			if aux > 1:
				aux-=1
	print(count)
	return lista


# [7,2,9,4,3,8,6,1]
# [8,4,2,5,3,6]

print(insertion_sort([7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1]))