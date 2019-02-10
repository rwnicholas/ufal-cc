#!/usr/bin/python3
class Celula:
	item = None
	proximo = None

	def __init__(self):
		self.item = None
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
		aux = self.fim
		self.fim = Celula()
		self.fim.proximo = None
		self.fim.item = item
		if aux != None:
			aux.proximo = self.fim
		aux = None
		if self.tamanho == 0:
			self.inicio = self.fim
		self.tamanho += 1


	def remover(self):
		if self.tamanho == 0:
			print("Fila vazia")
			return None
		aux = self.inicio
		self.inicio = self.inicio.proximo
		return aux.item

	def imprimir(self):
		aux = self.inicio
		while(aux != None):
			print(aux.item)
			aux = aux.proximo
		print("-----------------------------------------")



