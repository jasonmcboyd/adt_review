class Stack:
	class __Node:
		def __init__(self):
			self.array = []
			self.previous = None
			
	def __init__(self):
		self.__count = 0
		self.__index = -1
		self.__arraySize = 64
		self.__node = None
		
	def __len__(self):
		return self.__count
		
	def __iter__(self):
		node = self.__node
		while node != None:
			for i in range(1, len(node.array) + 1):
				yield node.array[-i]
			node = node.previous
	
	def push(self, value):
		self.__count += 1
		self.__index = (self.__index + 1) % self.__arraySize
		if self.__index == 0:
			node = self.__Node()
			node.previous = self.__node
			self.__node = node
		self.__node.array.append(value)
	
	def pop(self):
		if self.__count == 0:
			raise IndexError('There are no items on the stack.')
		result = self.__node.array.pop()
		self.__index -= 1
		if self.__index == -1:
			self.__node = self.__node.previous
			if self.__node != None:
				self.__index = self.__arraySize - 1
		self.__count -= 1
		return result