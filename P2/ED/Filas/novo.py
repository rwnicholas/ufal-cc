#!/usr/bin/python3

class Celula:
	valor = None
	proximo = None

	def __init__(self, valor):
		self.valor = valor
		self.proximo = None

class Fila:
	inicio = None
	fim = None
	tamanho = 0

	def __init__(self):
		self.inicio = None
		self.fim = None
		self.tamanho = 0

	def inserir(self, item):
		if self.vazio() == True:
			self.inicio = Celula(item)
			self.fim = self.inicio
		else:
			self.fim.proximo = Celula(item)
			self.fim = self.fim.proximo
		self.tamanho += 1
		
	def vazio(self):
		return self.tamanho == 0

	def imprimir(self):
		aux = self.inicio
		while(aux != None):
			print(aux.valor)
			aux = aux.proximo
		print("----------------------------------")

f = Fila()

f.inserir(2)
f.inserir(3)
f.inserir(4)
f.inserir(5)
f.imprimir()