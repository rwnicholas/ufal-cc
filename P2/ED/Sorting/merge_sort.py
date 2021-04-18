#!/usr/bin/python3

def merge_sort(lista):
	if len(lista) < 2:
		return lista
	meio = len(lista)//2
	lista1 = merge_sort(lista[:meio])
	lista2 = merge_sort(lista[meio:])
	final = []
	i = j = 0
	for x in range(len(lista1)+len(lista2)):
		if i == len(lista1):
			final.append(lista2[j])
			j+=1
		elif j == len(lista2):
			final.append(lista1[i])
			i+=1
		elif lista1[i] <= lista2[j]:
			final.append(lista1[i])
			i+=1
		else:
			final.append(lista2[j])
			j+=1
	return final

# [7,2,9,4,3,8,6,1]

print(merge_sort([7,2,9,4,3,8,6,1]))