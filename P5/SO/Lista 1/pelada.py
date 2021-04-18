#!/usr/bin/python3
from queue import PriorityQueue
import random
import threading
from datetime import datetime
import time

QTD_JOGADORES = 10

sumDePosse = 0
pq = PriorityQueue(maxsize=QTD_JOGADORES)
lock = threading.Lock()

## Define as prioridades de forma aleatória
def prioridadeJogador(listaPrioridades):
    x = random.randint(1,QTD_JOGADORES)
    
    while (x in listaPrioridades):
        x = random.randint(1,QTD_JOGADORES)
    
    listaPrioridades.append(x)

    return x

def jogador(name, priority):
    global sumDePosse

    lock.acquire()
    print("%s\tO jogador %s pega a bola (prioridade = %s)." %(datetime.now().strftime('%H:%M:%S'), name, priority))

    posseDeBola = 0.55 * priority ## A posse de bola será maior para quem tiver maior prioridade
    sumDePosse+=posseDeBola
    time.sleep(posseDeBola)

    print("%s\tO jogador %s perde a bola (prioridade = %s).\n" %(datetime.now().strftime('%H:%M:%S'), name, priority))
    lock.release()

## Aqui serão sorteadas QTD_JOGADORES prioridades de forma aleatória para atribuir aos jogadores
lp = []
for i in range(QTD_JOGADORES):
    prioridade = prioridadeJogador(lp)

    ## Sinal negativo na prioridade para que a PriorityQueue obedeça a ordem decrescente
    pq.put((-prioridade, threading.Thread(target=jogador, args=(i, prioridade))))

while not pq.empty():
    next_Jogador = pq.get()
    next_Jogador[1].start() ## Iniciando a thread
    next_Jogador[1].join() ## Aguardando a thread ser concluída

print("Média de posse de bola: %s segundos" %(sumDePosse/QTD_JOGADORES))