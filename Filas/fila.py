#!/usr/bin/python3

class Fila:
	inicio = None
	fim = None
	tamanho = None
	filaVetor = None

	def __init__(self,size):
		self.inicio = 0
		self.fim = 0
		self.tamanho = size
		self.filaVetor = [None]*size

	def filaCheia(self):
		if (self.inicio%self.tamanho) == (self.fim%self.tamanho) and self.filaVetor[self.fim%self.tamanho] != None:
			return True
		else:
			return False

	def filaVazia(self):
		if (self.inicio%self.tamanho) == (self.fim%self.tamanho) and self.filaVetor[self.inicio%self.tamanho] == None:
			return True
		else:
			return False

	#inserir
	def inserir(self,item):
		if self.filaCheia() == True:
			print("Fila Cheia")
			return None

		self.filaVetor[int(self.fim%self.tamanho)] = item
		self.fim += 1
	#remover
	def remover(self):
		if self.filaVazia() == True:
			print("Fila vazia")
			return None
		
		aux = self.filaVetor[int(self.inicio%self.tamanho)]
		self.filaVetor[int(self.inicio%self.tamanho)] = None
		self.inicio += 1
		return aux

	def imprimir(self):
		print(self.filaVetor)
	

