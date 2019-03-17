#!/usr/bin/python3

from lista import Lista
principal = Lista()
agenda = [('nick', 999), ('lucas', 444),('dudu', 666), ('gean', 616)]
def reorganizar(item):
	principal.inserir(item)
	no = principal.inicio.proximo
	while no != None:
		no2 = principal.inicio.proximo
		while no2 != None:
			if no != no2 and no.item < no2.item:
				index1 = principal.buscar(no.item)
				principal.remover(index1)
				principal.inserir(no2.item, index1)

				index2 = principal.buscar(no2.item)
				principal.remover(index2)
				principal.inserir(no.item, index2)

			no2 = no2.proximo
		no = no.proximo

for x in agenda:
	reorganizar(x)
	principal.imprimir()

				