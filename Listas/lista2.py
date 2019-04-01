#!/usr/bin/python3

class Celula:
	item = None
	proximo = None

	def __init__(self, item):
		self.item = item
		self.proximo = None

class Lista:
	inicio = None
	tamanho = 0

	def __init__(self):
		self.inicio = Celula(None)
		self.tamanho = 0

	#vazia
	def vazio(self):
		return self.tamanho == 0
	
	#inserir
	def inserir(self, item, pos = None):
		pos = pos if pos != None else self.tamanho
		if pos > self.tamanho or pos < 0:
			print("Posição não existe")
			return
		
		p = self.inicio
		for i in range(pos):
			p = p.proximo
		
		aux = p.proximo
		p.proximo = Celula(item)
		p.proximo.proximo = aux
		self.tamanho += 1
	
	#remover
	def remover(self, pos = None):
		pos = pos if pos != None else self.tamanho
		if pos >= self.tamanho or self.vazio() or pos < 0:
			print("Posição não existe, ou lista vazia")
			return
		
		p = self.inicio
		for i in range(pos):
			p = p.proximo

		aux  = p.proximo
		p.proximo = p.proximo.proximo
		item = aux.item
		del aux
		self.tamanho -= 1

		return item
	#imprimir
	def imprimir(self):
		p = self.inicio.proximo
		while p != None:
			print(p.item)
			p = p.proximo
		print("------------------")
	#buscar
	def buscar(self, item):
		p = self.inicio.proximo
		for i in range(self.tamanho):
			if p.item == item:
				return i
			p = p.proximo
		
		return None