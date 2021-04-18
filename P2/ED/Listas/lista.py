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
	
	def vazio(self):
		if self.tamanho == 0:
			return True
		return False

	def inserir(self, item, pos = None):
		# if pos == None:
			# pos = self.tamanho
		pos = pos if pos != None else self.tamanho
		if pos > self.tamanho:
			print("Posição",pos,"não existe!")
			return

		p = self.inicio
		for i in range(pos):
			p = p.proximo
		
		aux = p.proximo
		p.proximo = Celula(item)
		p.proximo.proximo = aux
		self.tamanho += 1
	
	def remover(self, pos = None):
		pos = pos if pos != None else self.tamanho
		if pos >= self.tamanho:
			print("Posição",pos,"não existe!")
			return
		if self.vazio() == True:
			print("Vazio")
			return
		
		p = self.inicio
		for i in range(pos):
			p = p.proximo
		item = p.proximo.item
		if p.proximo.proximo != None:
			aux = p.proximo.proximo
			p.proximo = p.proximo.proximo
			del aux
		else:
			del p.proximo

		self.tamanho -= 1
		return item

	def imprimir(self):
		p = self.inicio.proximo
		while p != None:
			print(p.item)
			p = p.proximo
		print("--------------")

	# def retornar(self):
	# 	tmp = []
	# 	p = self.inicio.proximo
	# 	while p != None:
	# 		print(p.item)
	# 		p = p.proximo
		
	def buscar(self, item):
		p = self.inicio.proximo
		for i in range(self.tamanho):
			if p.item == item:
				return i
			p = p.proximo
		return None
