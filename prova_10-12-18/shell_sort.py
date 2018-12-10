#!/usr/bin/python3

def shell_sort(lista):
	count = 0
	h = setH(lista)
	while h != 1:
		h = h//3
		for i in range(h,len(lista)):
			count+=1
			aux = i
			while (lista[aux-1] > lista[aux]):
				lista[aux-1],lista[aux] = lista[aux],lista[aux-1]
				if aux > 1:
					aux-=h
	print(count)
	return lista
def setH(lista):
	h = 1
	while (h * 3) + 1 < len(lista):
		h = (h * 3) + 1
		#print(h)
	return h
# [7,2,9,4,3,8,6,1]
# [8,4,2,5,3,6]

print(shell_sort([7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1]))