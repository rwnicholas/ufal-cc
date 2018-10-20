#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

cidades = []

def retornarValor(cidade):
	url = "https://cidades.ibge.gov.br/brasil/al/" + cidade

	html_content = urlopen(url)
	soup = BeautifulSoup(html_content, 'lxml')
	matches = soup.find_all("div", {"class":"indicador__valor"})
	if matches == []:
		url = "https://cidades.ibge.gov.br/brasil/al/" + cidade + "/panorama"
		html_content = urlopen(url)
		soup = BeautifulSoup(html_content, 'lxml')
		matches = soup.find_all("div", {"class":"indicador__valor"})
	
	#Determinando o match
	for elemento in matches:
		if 'R$' in elemento.get_text(strip=True)[-2:]:
			match = elemento.get_text(strip=True)
			return match
	return None

with open("Alagoas.txt", "r") as entrada:
	for linha in entrada:
		cidadeTemp = ""
		for i in range(len(linha)):
			if (linha[i] == ','):
				cidadeTemp = linha[:i]
				cidadeTemp = cidadeTemp.lower()
				for j in range(len(cidadeTemp)):
					if (cidadeTemp[j] == ' '):
						cidadeTemp = cidadeTemp[:j] + '-' + cidadeTemp[j+1:]
				print(retornarValor(cidadeTemp))
				print(cidadeTemp)
				break
