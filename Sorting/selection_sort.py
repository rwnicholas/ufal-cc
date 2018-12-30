#!/usr/bin/python3

def selection_sort(lista):
	count = 0
	for i in range(len(lista)-1):
		menor = i
		for j in range(i,len(lista)):
			count+=1
			if lista[j] < lista[menor]:
				menor = j
		if (lista[i] > lista[menor]):
			lista[i],lista[menor] = lista[menor],lista[i]
	print(count)
	return lista


# [7,2,9,4,3,8,6,1]
# [8,4,2,5,3,6]

print(selection_sort([8,4,2,5,3,6]))