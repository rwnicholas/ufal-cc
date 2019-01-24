#!/usr/bin/python3
class Stack:
	position = None
	stackList = None
	length = None

	def __init__(self, length):
		self.length = length
		self.stackList = [None]*length
		self.position = -1

	def pop(self):
		if(self.position > -1):
			self.stackList[self.position] = None
			self.position-=1
	
	def push(self, value):
		if(self.position+1 < self.length):
			self.position+=1
			self.stackList[self.position] = value
	
	def isItVoid(self):
		if(self.position == -1):
			return True
		return False

	def lenStack(self):
		return self.position+1

	def printStack(self):
		print(self.stackList)
