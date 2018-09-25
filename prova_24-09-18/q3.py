#!/usr/bin/python3

#hoteisG = [('hotel0', 300, 100, 5), ('hotel1', 100, 900, 3), ('hotel2', 400, 100, 4), ('hotel3', 300, 200, 5)]
hoteisG = [('hotel0', 160, 200, 4), ('hotel1', 160, 400, 3), ('hotel2', 560, 100, 5)]

def melhoresHoteis(hoteis):
	pioresHoteis = []
	for hotel in range(len(hoteis)):
		for outro in range(hotel+1,len(hoteis)):
			preco1 = hoteis[outro][1]
			preco2 = hoteis[hotel][1]
			dist1 = hoteis[outro][2]
			dist2 = hoteis[hotel][2]
			quali1 = hoteis[outro][3]
			quali2 = hoteis[hotel][3]

			if (preco1 >= preco2 and dist1 >= dist2 and quali1 < quali2):
				pioresHoteis.append(outro)
			elif (preco1 >= preco2 and dist1 > dist2 and quali1 <= quali2):
				pioresHoteis.append(outro)
			elif (preco1 > preco2 and dist1 >= dist2 and quali1 <= quali2):
				pioresHoteis.append(outro)
	hoteisFinais = []

	for hotel in range(len(hoteis)):
		if not hotel in pioresHoteis:
			hoteisFinais.append(hoteis[hotel])
	return hoteisFinais

print(melhoresHoteis(hoteisG))
