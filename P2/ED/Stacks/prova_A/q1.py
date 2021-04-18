#!/usr/bin/python3

from stack_A import Pilha

principal = Pilha()
auxiliar = Pilha("auxiliar")
prioridade = None

def addTarefa(prior,item):
	global principal
	global auxiliar

	if principal.tamanho == 0:
		principal.push(item,prior)
		return True
	
	while (principal.topo != None) and (principal.topo.prioridade > prior):
		tmp = principal.pop()
		auxiliar.push(tmp.valor,tmp.prioridade)
	principal.push(item,prior)
	auxiliar.printStack()
	# principal.printStack()

	while (auxiliar.topo != None) and (auxiliar.tamanho != 0):
		tmp = auxiliar.pop()
		principal.push(tmp.valor, tmp.prioridade)
	
	principal.printStack()
	# auxiliar.printStack()
def resolver():
	global principal
	principal.pop()

user = None
while user != 3:
	user = int(input("0- Imprimir tarefas\n1- Adicionar Tarefa\n2- Resolver Tarefa Mais Importante\n3- Sair\n"))
	if user == 3:
		break
	elif user == 2:
		resolver()
		principal.printStack()
		continue
	elif user == 0:
		principal.printStack()
		continue
	elif user != 1:
		print("Opção não disponível")
		continue
	
	while prioridade != 0:
		prioridade = int(input("Qual a prioridade da tarefa? (Digite 0 para não adicionar mais) "))
		
		if prioridade == 0:
			break
		
		if not prioridade in range(1,5+1):
			print("Prioridade errada")
			continue

		item = input("Qual a tarefa? ")
		addTarefa(prioridade,item)
	print("------------------ Finalizando ---------------------\n\n\n")
	principal.printStack()