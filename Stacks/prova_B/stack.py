#!/usr/bin/python3

class Celula:
	valor = None
	proximo = None
	fixada = 0
	
	def __init__(self):
		self.valor = None
		self.proximo = None
		self.fixada = None
	
class Pilha:
	topo = None
	tamanho = 0
	
	def __init__(self):
		self.topo = None
		self.tamanho = 0
		
	#push
	def push(self, valor, fixa = 0):
		aux = self.topo
	
		self.topo = Celula()
		self.topo.valor = valor
		self.topo.fixada = fixa
		self.topo.proximo = aux
		self.tamanho+=1
		print("Inserindo",self.topo.valor,"no endereço",self.topo)
		
	#pop
	def pop(self):
		if self.tamanho == 0:
			print("Pilha vazia")
			return None
		aux = self.topo
		self.topo = self.topo.proximo
		self.tamanho-=1
		print("Removendo",aux.valor,"do endereço",aux)
		return aux
		
	#stackPrint
	def stackPrint(self):
		if self.tamanho == 0:
			print("Pilha vazia")
			return None
		
		aux = self.topo
		while aux != None:
			if aux != None:
				print("|",aux.valor,"|")
				aux = aux.proximo
		
		print("--------------- Fim ----------------")
		
		
	
