#!/usr/bin/python3

from fila_D import Fila

principal = Fila()
auxiliar = Fila()

pacotes = [5,4,3,2,1]

for x in pacotes:
	auxiliar.inserir(x)

while auxiliar.tamanho != 0:
	aux = auxiliar.remover()
	if aux == 1 or (principal.tamanho != 0) and (aux == principal.fim.item + 1):
		principal.inserir(aux)
	else:
		auxiliar.inserir(aux)
	
auxiliar.imprimir()
principal.imprimir()
