#!/usr/bin/python3

from stack_A import Pilha

senha = "aaabbccddd"

def popular(senha):
	tmp = Pilha()
	
	for i in range(len(senha)//2):
		tmp.push(senha[i])
	return tmp

def valida(senha):
	if len(senha)%2 != 0:
		return False
	pilha = popular(senha)
	aux = senha[len(senha)//2:]
	
	for x in aux:
		if pilha.tamanho != 0 and x == 'c' and pilha.pop().valor != 'b':
			return False
		elif pilha.tamanho != 0 and x == 'd' and pilha.pop().valor != 'a':
			return False

	if pilha.tamanho != 0:
		return False
	pilha.printStack()

	return True

if valida(senha) == True:
	print("Senha: %s é válida" %senha)
else:
	print("Senha: %s é inválida" %senha)