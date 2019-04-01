#!/usr/bin/python3

from lista2 import Lista
principal = Lista()
agenda = [('nick', 999), ('lucas', 444), ('fillipe', 555),('dudu', 666), ('gean', 616)]
def reorganizar(item):
	principal.inserir(item)
	no = principal.inicio.proximo
	while no != None:
		no2 = principal.inicio.proximo
		menor = no.item
		while no2 != None:
			if no != no2 and no.item[0] > no2.item[0]:
				menor = no2.item
		
			no2 = no2.proximo

		index2 = principal.buscar(menor)
		principal.remover(index2)
		principal.inserir(no.item, index2)

		index1 = principal.buscar(no.item)
		principal.remover(index1)
		principal.inserir(menor, index1)
		no = no.proximo

for x in agenda:
	reorganizar(x)
	principal.imprimir()

				