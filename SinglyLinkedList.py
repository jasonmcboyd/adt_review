class SinglyLinkedListNode:
	def __init__(self, value):
		self._next = None
		self.value = value
		self.__linkedList = None

class SinglyLinkedList:
	def __init__(self, list = []):
		self._head = None
		self._tail = None
		self._count = 0
		for i in list:
			self.addLast(i)
	
	def __len__(self):
		return self._count
	
	def __iter__(self):
		node = self._head
		while node != None:
			yield node.value
			node = node._next
	
	def first(self):
		return self._head
		
	def last(self):
		return self._tail
	
	def addLast(self, value):
		if (self._tail == None):
			self._head = SinglyLinkedListNode(value)
			self._tail = self._head
		else:
			self._tail._next = SinglyLinkedListNode(value)
			self._tail = self._tail._next
		self._count += 1
		self._tail.__linkedList = self
	
	def addFirst(self, value):
		if (self._head == None):
			self._head = SinglyLinkedListNode(value)
			self._tail = self._head
		else:
			node = SinglyLinkedListNode(value)
			node._next = self._head
			self._head = node
		self._count += 1
		self._head.__linkedList = self
			
	def addAfter(self, node, value):
		if node.__linkedList != self:
			raise ValueError('The node is not a member of this linked list.')
		newNode = SinglyLinkedList(value);
		newNode.__linkedList = self
		newNode._next = node._next
		node._next = newNode
		self._count += 1
		
	def findFirst(self, value, startNode = None):
		node = startNode
		if node == None:
			node = self._head
		while node != None:
			if node.value == value:
				return node
			else:
				node = node._next
		return None
	
	def findAll(self, value):
		node = self.findFirst(value)
		while node != None:
			yield node
			node = None if node._next == None else self.findFirst(node._next)
	
	def removeNode(self, node):
		if node.__linkedList != self:
			raise ValueError('The node is not a member of this linked list.')
		p1 = None
		p2 = self._head
		while p2 != node:
			p1 = p2
			p2 = p2._next
		if p1 != None:
			p1._next = p2._next
		else:
			self._head = p2._next
		p2._next = None
		p2.__linkedList = None
		self._count -= 1
	
	def clear(self):
		node = self._head
		while node != None:
			temp = node
			node = node._next
			temp._next = None
			temp.__linkedList = None
		self._head = None
		self._tail = None
		self._count = 0
		
	def reverseInPlace(self):
		if self._count < 2:
			return
			
		head = self._head._next
		self._head._next = None
		self._tail = self._head
		
		while head != None:
			temp = head._next
			head._next = self._head
			self._head = head
			head = temp