#!/usr/bin/python3

from stack import Stack

pilha = Stack(5)

pilha.push("nicholas")
pilha.push("eduardo")
pilha.push("lucas")
pilha.push("666")

pilha.printStack()
print(pilha.isItVoid())
print(pilha.lenStack())
pilha.pop()

pilha.printStack()
print(pilha.isItVoid())
print(pilha.lenStack())
pilha.pop()

pilha.printStack()
print(pilha.isItVoid())
print(pilha.lenStack())
pilha.pop()

pilha.printStack()
print(pilha.isItVoid())
print(pilha.lenStack())
pilha.pop()

pilha.printStack()
print(pilha.isItVoid())
print(pilha.lenStack())
pilha.pop()