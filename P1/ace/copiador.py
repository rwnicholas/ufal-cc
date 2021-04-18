#!/usr/bin/python3
import csv

pib = []

def retornarValor():
	output = []
	with open("mapa.csv") as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in csv_reader:
			output.append(row[1][1:])
	return output

pib = retornarValor()
count = 0
with open('Alagoas.csv', 'r') as fin:
	reader = csv.reader(fin, delimiter=',')
	with open('output.csv', 'w') as fout:
		writer = csv.writer(fout, delimiter=',')
		for row in reader:
			row.append(pib[count])
			writer.writerow(row)
			count+=1