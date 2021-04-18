#!/usr/bin/python3
notas = {}

def mediaAluno(nome):
	return (notas[nome][0] + notas[nome][1]) / 2

nome = None
nota1 = None
nota2 = None

while(nome != ""):
	nome = input("Nome do aluno: ")
	if (nome != ""):
		notas1 = float(input("Nota 1: "))
		notas2 = float(input("Nota 2: "))
		notas[nome] = (notas1, notas2)

print(mediaAluno("Nicholas"))
print(mediaAluno("Eduardo"))
print(mediaAluno("Fulano"))