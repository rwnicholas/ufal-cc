#!/usr/bin/python3

from lista2 import Lista

principal = Lista()
tmp = [1,2,3,4,5,6,7,8,9,10]
for x in tmp:
	principal.inserir(x)

def somaDeDois(valor):
	no = principal.inicio.proximo
	while no != None:
		no2 = principal.inicio.proximo
		while no2 != None:
			if no != no2 and (no.item + no2.item == valor):
				print(no.item)
				print(no2.item)
				return True
			no2 = no2.proximo
		no = no.proximo
	
	return False

print(somaDeDois(15))