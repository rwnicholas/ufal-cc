#!/usr/bin/python3

class Celula:
	item = None
	proximo = None

	def __init__(self, item):
		self.item = item
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
		if self.vazio():
			self.inicio = Celula(item)
			self.fim = self.inicio
		else:
			self.fim.proximo = Celula(item)
			self.fim = self.fim.proximo

		self.tamanho += 1

	def remover(self):
		aux = self.inicio
		if self.vazio():
			print("Fila vazia")
			return False
		self.inicio = self.inicio.proximo
		self.tamanho -= 1

		valor = aux.item
		del aux
		return valor

	def vazio(self):
		return self.tamanho == 0

	def imprimir(self):
		aux = self.inicio
		while(aux != None):
			print(aux.item)
			aux = aux.proximo
		print("----------------------------------")