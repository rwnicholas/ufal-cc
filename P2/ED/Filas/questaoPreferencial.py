#!/usr/bin/python3

from fila_D import Fila

senhas = ['n1','n2','n3','p1','n4','p2','n5','n6','p3']

preferencial = Fila()
normal = Fila()

for x in senhas:
	if 'n' in x:
		normal.inserir(x)
	else:
		preferencial.inserir(x)

while not normal.vazio() or not preferencial.vazio():
	if not preferencial.vazio():
		print(preferencial.remover())
	if not normal.vazio():
		print(normal.remover())