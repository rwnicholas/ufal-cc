#!/usr/bin/python3

from fila_D import Fila

f = Fila()

f.inserir(2)
f.imprimir()
f.inserir(3)
f.imprimir()
f.inserir(4)
f.imprimir()

f.remover()
f.imprimir()

f.inserir(5)
f.imprimir()

f.remover()
f.imprimir()

f.inserir(6)
f.imprimir()
f.remover()
f.remover()
f.remover()
f.remover()
f.imprimir()