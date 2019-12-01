#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.DiGraph()
entrada = []
d = 0.875

while True:
	try:
		entrada.append(input())
	except EOFError:
		break
grafo.add_nodes_from(entrada[0].split())
for n in grafo.nodes():
	grafo.add_node(n, weight=1/grafo.number_of_nodes(), PR=1/grafo.number_of_nodes())
for i in range(1, len(entrada)-1):
	u,v=entrada[i].split(" -> ")
	if(u != v):
		grafo.add_edge(u,v)


for x in grafo.nodes():
	print(x, "->", list(grafo.successors(x)))
	print(list(grafo.predecessors(x)), "->", x)

# nx.draw(grafo, with_labels=True)
# plt.show()

def getSumOfPRO(dicio, skipNode):
	PRO = 0
	# weightByNode = nx.get_node_attributes(grafo, 'weight')
	for key in dicio:
		if key != skipNode and (len(list(grafo.successors(key))) != 0):
			PRO += (dicio[key]/len(list(grafo.successors(key))))
	return PRO
		
# def pagerank():
# 	for i in range(0, int(entrada[len(entrada)-1])+1):
# 		print("PageRank (passo %d)" %(i))
# 		listaDeNodes = list(grafo.nodes(data='weight'))
# 		for elemento in listaDeNodes:
# 			print("%s: %.3f" %(elemento[0], elemento[1]))
# 		for x in grafo.nodes:
# 			pr = (1 - d)/grafo.number_of_nodes() + d * getSumOfPRO(x)
# 			print(pr)
# 			grafo.add_node(x, PR=pr)

# 		novosPesos = list(grafo.nodes(data='PR'))
# 		for elemento in novosPesos:
# 			grafo.add_node(elemento[0], weight=elemento[1])

def pagerankMain():
	#inicializando os pesos
	dicionarioNodes = dict(grafo.nodes())
	for key in dicionarioNodes:
		dicionarioNodes[key] = 1/grafo.number_of_nodes()
	
	for i in range(0, int(entrada[len(entrada)-1])+1):
		auxDicio = dicionarioNodes.copy()
		print("PageRank (passo %d)" %(i))
		for key in dicionarioNodes:
			print("%s: %.3f" %(key, dicionarioNodes[key]))
		for n in auxDicio:
			pr = (1-d)/grafo.number_of_nodes() + d * getSumOfPRO(dicionarioNodes, n)
			auxDicio[n] = pr
		dicionarioNodes = auxDicio.copy()
		

pagerankMain()