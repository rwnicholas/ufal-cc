#!/usr/bin/python3

class TabHash:
	size = None
	itens = None
	tamanhoElementos = 0

	def __init__(self, size):
		self.size = size
		self.itens = [None]*self.size
		self.tamanhoElementos = 0

	def calcHash(self, chave):
		return chave % self.size

	def inserir(self, chave):
		if(self.itens[self.calcHash(chave)] == None):
			self.itens[self.calcHash(chave)] = []
		self.itens[self.calcHash(chave)].append(chave)
		self.tamanhoElementos += 1

	def remover(self, chave):
		if self.itens[self.calcHash(chave)] != None:
			if chave in self.itens[self.calcHash(chave)]:
				self.itens[self.calcHash(chave)].remove(chave)
				self.tamanhoElementos -= 1
			else:
				print("Chave não existe")

			if len(self.itens[self.calcHash(chave)]) == 0:
				self.itens[self.calcHash(chave)] = None
		else:
			print("Chave não existe")


	def imprimir(self):
		for i in range(len(self.itens)):
			print("%d: %s" %(i, self.itens[i]))
			i+=1
		print("------------------")
