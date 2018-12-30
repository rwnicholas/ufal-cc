#!/usr/bin/python3

totalDic = {}
texto = "aabbbddçaldskfjadoweiruqpiorudlsakfjoqeru"

def contVogal(texto):
	for c in set(texto):
		if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
			totalDic[c] = texto.count(c)

contVogal(texto)
print(totalDic)