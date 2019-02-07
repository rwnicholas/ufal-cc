#!/usr/bin/python3

from stack_fixa import Pilha

exp = "5 6 + 1 2 + *"
exp = "1 2 + 3 *"



def resolver(exp):
	tmp = Pilha(len(exp))

	for x in exp.split():
		if not x in "*+/-":
			tmp.push(x)
		elif x == '*':
			aux = tmp.pop()
			while tmp.topo != -1:
				aux*=int(tmp.pop())
				print("*",aux)
			tmp.push(aux)
			aux = None
		elif x == '+':
			aux = tmp.pop()
			while tmp.topo != -1:
				aux +=int(tmp.pop())
				print(aux)
			tmp.push(aux)
			aux = None

		elif x == '/':
			aux = tmp.pop()
			while tmp.topo != -1:
				aux /=int(tmp.pop())
				print(aux)
			tmp.push(aux)
			aux = None
		elif x == '-':
			aux = tmp.pop()
			while tmp.topo != -1:
				aux -=int(tmp.pop())
				print(aux)
			tmp.push(aux)
			aux = None
	print(tmp.pop())
#	return final

#print(resolver(exp))
resolver(exp)
		
