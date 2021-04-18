#!/usr/bin/python3

#inverter números sem strings

def inverte(num):
	output = 0
	tam = len(str(num)) - 1

	while (num > 0):
		resto = num % 10
		num = num // 10
		output+= resto * (10 ** tam)
		tam -= 1
	
	return output

print(inverte(int(input("Valor: "))))