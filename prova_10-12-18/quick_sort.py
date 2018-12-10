#!/usr/bin/python3

def quick_sort(lista):
	if len(lista) < 2:
		return lista
	print(lista)
	pivo = lista[0]
	left = []
	right = []
	for x in range(1,len(lista)):
		if lista[x] <= pivo:
			left.append(lista[x])
		else:
			right.append(lista[x])
		
	return quick_sort(left) + [pivo] + quick_sort(right)

# [7,2,9,4,3,8,6,1]
# [8,4,2,5,3,6]

print(quick_sort([7,2,9,4,3,8,6,1]))