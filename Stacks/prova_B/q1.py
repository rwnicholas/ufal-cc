#!/usr/bin/python3


from stack import Pilha

principal = Pilha()
auxiliar = Pilha()

def inserirPostagem(post,user):
	global principal
	global auxiliar
	
	if principal.tamanho == 0 or user == 1:
		principal.push(post,user)
		return True
	
	while principal.topo != None and principal.topo.fixada == 1:
		aux = principal.pop()
		auxiliar.push(aux.valor,aux.fixada)

	principal.push(post,user)
	
	while auxiliar.tamanho != 0:
		aux = auxiliar.pop()
		principal.push(aux.valor,aux.fixada)
		
	
user = None

while user != 2:
	user = int(input("Postagem fixa?\n0- Não\n1- Sim\n2- Sair\n"))
	if user != 2:
		post = input("Conteúdo da Postagem ")
		print(post)
		inserirPostagem(post,user)
	else:
		principal.stackPrint()
