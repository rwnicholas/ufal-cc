#!/usr/bin/python3

class Celula:
	prioridade = None
	valor = None
	proximo = None
	
	def __init__(self, item, importancia):
		self.prioridade = importancia
		self.valor = item
		self.proximo = None

class Pilha:
	topo = None
	tamanho = 0
	tipo = None

	def __init__(self, tipo = "normal"):
		self.topo = None
		self.tamanho = 0
		self.tipo = tipo

	def push(self, item, importancia = -1):
		tmp = self.topo
		self.topo = Celula(item, importancia)
		self.topo.proximo = tmp
		self.tamanho+=1
		print("Item:",item,"inserido em uma pilha",self.tipo,"no endereço:",self.topo)
		tmp = None
		del tmp
	
	def pop(self):
		if self.tamanho == 0:
			print("Pilha vazia")
			return None

		tmp = self.topo
		self.topo = self.topo.proximo
		print("Item:",tmp.valor,"removido de uma pilha",self.tipo,"endereço:",tmp)
		self.tamanho-=1
		return tmp
		# del tmp

	def printStack(self):
		tmp = self.topo
		if tmp == None:
			print("Pilha",self.tipo,"vazia")
			return None
		print("------------------------Começo de Pilha",self.tipo,"----------------------")
		while tmp != None:
			if (tmp.prioridade != -1):
				print("|",tmp.prioridade,"|",tmp.valor,"|")
			else:
				print("|",tmp.valor,"|")
			if tmp.proximo != None:
				tmp = tmp.proximo
			else:
				print("------------------------Fim de Pilha",self.tipo,"----------------------\n")
				return None

