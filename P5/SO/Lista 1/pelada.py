#!/usr/bin/python3
from queue import PriorityQueue
import random
import threading
from datetime import datetime
import time

sumDePosse = 0
pq = PriorityQueue(maxsize=10)
lock = threading.Lock()

def prioridadeJogador(listaPrioridades):
    x = random.randint(1,10)
    
    while (x in listaPrioridades):
        x = random.randint(1,10)
    
    listaPrioridades.append(x)

    return x

def jogador(name, priority):
    global sumDePosse

    print("%s\tO jogador %s pega a bola (prioridade = %s)." %(datetime.now().strftime('%H:%M:%S'), name, priority))
    lock.acquire()

    posseDeBola = 0.55 * priority
    sumDePosse+=posseDeBola
    time.sleep(posseDeBola)

    lock.release()
    print("%s\tO jogador %s perde a bola (prioridade = %s).\n" %(datetime.now().strftime('%H:%M:%S'), name, priority))

lp = []
for i in range(10):
    prioridade = prioridadeJogador(lp)
    pq.put((-prioridade, threading.Thread(target=jogador, args=(i, prioridade))))

while not pq.empty():
    next_Jogador = pq.get()
    next_Jogador[1].run()

print(sumDePosse/10)