#!/usr/bin/python3

from stack import Stack

# exp = "3-[15+2*(4-3)*[2+(5-1)]]/4"
exp = "5-[4+(0-3]"
print(exp)

def charInList(c, list):
	for x in list:
		if x == c:
			return True
	return False

def wellConstructed(pilha):
	finalDecision = True
	tmp = []
	for i in range(pilha.lenStack()):
		char = pilha.pop()
		if char == ']':
			tmp.append('[')
			continue
		elif char == ')':
			tmp.append('(')
			continue
	
		if char == '(' or char == '[':
			if charInList(char, tmp) == True:
				tmp.remove(char)
			else:
				finalDecision = False
	if len(tmp) != 0:
		finalDecision = False
	return finalDecision

def constructStack(expTmp):
	tmpPilha = Stack(100)

	for x in expTmp:
		tmpPilha.push(x)

	return tmpPilha

p = constructStack(exp)

print(wellConstructed(p))
p.printStack()


