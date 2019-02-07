#!/usr/bin/python3
	
class Pilha:
	topo = -1
	vetor = None
	
	def __init__(self,size):
		self.topo = -1
		# self.vetor = [None]*size
		self.vetor = [None]*size
		
	#push
	def push(self, valor):
		self.topo+=1
		self.vetor[self.topo] = valor
#		print("Inserindo",self.topo.valor,"no endereço",self.topo)
		
	#pop
	def pop(self):
		if self.topo == -1:
			print("Pilha vazia")
			return None
		aux = self.vetor[self.topo]	
		print(aux)
		self.vetor[self.topo] = None
		self.topo-=1
#		print("Removendo",aux.valor,"do endereço",aux)
		return int(aux)
		
	#stackPrint
	def stackPrint(self):
		print(self.vetor)
		
		
	
