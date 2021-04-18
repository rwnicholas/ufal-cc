#!/usr/bin/python3
from urllib.request import urlopen
from robobrowser import RoboBrowser
import requests
from bs4 import BeautifulSoup
#https://servicodados.ibge.gov.br/api/v1/pesquisas/-/periodos/2015/indicadores/47001/resultados/270030
cidades = []

def getIdCidade(cidade):
	browser = RoboBrowser(parser='html.parser')
	browser.open("http://www.roseno.info/cidadesconsulta.aspx")
	form = browser.get_form(action="cidadesconsulta.aspx?")
	form['vCIDADENOM'] = cidade
	browser.submit_form(form)
	idTemp = browser.select('span_CIDADEIBGE_0003')
	browser.follow_link(idTemp)
	print(idTemp)
	print(browser)


def retornarValor(cidade):
	url = "https://cidades.ibge.gov.br/brasil/al/" + cidade

	# html_content = urlopen(url)
	# soup = BeautifulSoup(html_content, 'lxml')
	# matches = soup.find_all("div", {"class":"indicador__valor"})
	# if matches == []:
	# 	url = "https://cidades.ibge.gov.br/brasil/al/" + cidade + "/panorama"
	# 	html_content = urlopen(url)
	# 	soup = BeautifulSoup(html_content, 'lxml')
	# 	matches = soup.find_all("div", {"class":"indicador__valor"})
	
	# #Determinando o match
	# for elemento in matches:
	# 	if 'R$' in elemento.get_text(strip=True)[-2:]:
	# 		match = elemento.get_text(strip=True)
	# 		return match
	html_content = requests.get(url).content
	soup = BeautifulSoup(html_content, 'lxml')
	matches = soup.find_all("div", {"class":"indicador__valor"})
	if matches == []:
		url = "https://cidades.ibge.gov.br/brasil/al/" + cidade + "/panorama"
		html_content = requests.get(url).content
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
				getIdCidade(cidadeTemp)
				print(cidadeTemp)
				
				break
