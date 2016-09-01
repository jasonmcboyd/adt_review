class MinHeap:
	def __init__(self):
		self._array = []

	def _getParentIndex(self, index):
		if index == 0:
			return -1
		else:
			if index % 2 == 0:
				return (index // 2) - 1
			else:
				return (index - 1) // 2

	def insert(self, value):
		self._array.append(value)
		i = len(self._array) - 1
		j = self._getParentIndex(i)
		while j >= 0 and self._array[i] < self._array[j]:
			self._array[i], self._array[j] = self._array[j], self._array[i]
			i, j = j, self._getParentIndex(j)
			