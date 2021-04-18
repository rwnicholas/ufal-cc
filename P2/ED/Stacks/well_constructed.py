#!/usr/bin/python3

from stack import Stack

exp = "3-[15+2*(4-3)*[2+(5-1)]]/4"
# exp = "5-[4+(0-3]"
print(exp)
# [()]

def charInList(c, list):
	for x in list:
		if x == c:
			return True
	return False

def wellConstructed(expTmp):
	finalDecision = True
	pilha = Stack(10)

	for x in expTmp:
		if(x == '{' or x == '[' or x == '('):
			pilha.push(x)

		if x == ')' and pilha.pop != '(':
			finalDecision = False
			print(x)
		elif x == ']' and pilha.pop != '[':
			finalDecision = False
			print(x)
		elif x == '}' and pilha.pop != '{':
			finalDecision = False
			print(x)

	pilha.printStack()
	return finalDecision

print(wellConstructed(exp))
