#!/usr/bin/python3

def merge_sort(lista):
	final = lista
	tamanho = 1
	while tamanho < len(lista)-1:
		tmp = []
		for i in range(1,(len(lista)//tamanho)+1, 2):
			if (len(lista)//tamanho)%2 == 0:
				tmp.append(organizar(final[i-1],final[i]))
			else:
				tmp.append(organizar(final[i-1],final[i-1]))
		final = tmp
		tamanho*=2
	return final[0]
def organizar(lista1, lista2):
	final = []
	i = j = 0
	if isinstance(lista1, int) == True:
		lista1 = [lista1]
		lista2 = [lista2]
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

print(merge_sort([8,4,2,5,3,6]))