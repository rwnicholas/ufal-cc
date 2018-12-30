#!/usr/bin/python3

agendaTele = {}

def incluirNovoNome(nome, listaTelefones):
	agendaTele[nome] = listaTelefones

def incluirTelefone(nome, telefone):
	if not(nome in agendaTele.keys()):
		resposta = int(input("Nome não encontrado, deseja incluir?\n 1) Sim\n 2) Não\n"))
		if (resposta == 1):
			incluirNovoNome(nome, telefone)
	else:
		agendaTele[nome].append(telefone)

def excluirNome(nome):
	del agendaTele[nome]

def excluirTelefone(nome, telefone):
	if (len(agendaTele[nome]) == 1):
		excluirNome(nome)
	else:
		agendaTele[nome].remove(telefone)

def consultarTelefone(nome):
	return agendaTele[nome]

print(agendaTele)	
incluirNovoNome("Nicholas", [82981830626, 82999451234])
print(agendaTele)
incluirNovoNome("Rosemary", [82999857904])
print(agendaTele)

incluirTelefone("Nicholas", 66666666666)
print(agendaTele)
incluirTelefone("Eduardo", 4567863)
print(agendaTele)
excluirNome("Eduardo")
print(agendaTele)
excluirTelefone("Nicholas", 82999451234)
print(agendaTele)
excluirTelefone("Rosemary", 82999857904)
print(agendaTele)

print("Nicholas:", consultarTelefone("Nicholas"))