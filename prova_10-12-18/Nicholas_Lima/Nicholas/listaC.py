#!/usr/bin/python3
import csv

pib = []

def retornarValor():
	output = []
	with open("lista.csv") as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in csv_reader:
			aux = tuple(row)
			output.append(aux)
	return output

pib = retornarValor()