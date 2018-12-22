#!/usr/bin/python3
#Já que ela deve ser ordenada a cada inserção, a forma mais eficiente é a que faz o menor número de comparações para um lista que teoricamente já estará ordenada, pois a cada inserção a lista lista é ordenada.
count = 0

import listaC
# def insertion_sort(lista):
# 	global count
# 	count = 0
# 	for i in range(1, len(lista)):
# 		aux = i
# 		while lista[aux-1] > lista[aux]:
# 			count+=1
# 			lista[aux-1],lista[aux] = lista[aux],lista[aux-1]
# 			if aux > 1:
# 				aux-=1
# 	return lista

# def shell_sort(lista):
# 	global count
# 	h = setH(lista)
# 	while h!=1:
# 		h = h//3
# 		for i in range(h, len(lista)):
# 			aux = i
# 			while lista[aux-h] > lista[aux]:
# 				count+=1
# 				lista[aux-h],lista[aux] = lista[aux],lista[aux-h]
# 				aux-=h
# 				if aux < h:
# 					break
# 	return lista

# def setH(lista):
# 	h = 1
# 	while (3*h)+1 < len(lista):
# 		h = (3*h)+1
# 	return h

def insertion_sort(lista):
	global count
	for i in range(len(lista)):
		j = i
		while(j > 0 and lista[j] < lista[j-1]):
			count+=1
			lista[j],lista[j-1] = lista[j-1],lista[j]
			j-=1
	return lista

def shell_sort(lista):
	size = len(lista)
	global count
	count = 0
	h=1
	while(3*h + 1 < size):
		h = 3*h+1

	while(h >= 1):
		for i in range(h,size):
			j = i
			while(j - h >= 0 and lista[j] < lista[j-h]):
				count+=1
				lista[j],lista[j-h] = lista[j-h],lista[j]
				j -= h
		h = h//3

	return lista


def merge_sort(lista):
	if(len(lista) > 1):
		meio = len(lista)//2
		l1 = merge_sort(lista[:meio])
		l2 = merge_sort(lista[meio:])
		return merge(l1,l2)
	return lista

def merge(a, b):
	global count
	i=0;j=0
	aux = []
	while(i < len(a) and j < len(b)):
		if(a[i] < b[i]):
			aux.append(a[i]); i+=1
			count+=1
		else:
			aux.append(b[j]); j+=1
			count+=1
	while(i<len(a)):
		aux.append(a[i]); i+=1
		count+=1
	while(j<len(b)):
		aux.append(b[j]); j+=1
		count+=1
	return aux

def selection_sort(lista):
	tam = len(lista)
	for i in range(tam):
		m=i
		for j in range(i,tam):
			if(lista[j] < lista[m]):
				m=j
		lista[m],lista[i] = lista[i],lista[m]
	return lista

def agendaTelefonica():
	data = listaC.pib
	agenda = []
	#inserir em Agenda 
	for x in range(len(data)):
		agenda.append(data[x])
		agenda = selection_sort(agenda)
	return agenda

print(agendaTelefonica())
print(count)