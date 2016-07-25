class Fib:
	def __init__(self, max):
		self.N = max
		self.count = 0
	def __iter__(self):
		self.a = 0
		self.b = 1
		return self
	def next(self): #python2
	#def __next__(self):#python3
		fib = self.a
		self.count += 1
		if self.count == self.N + 1:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib

for x in Fib(int(input())):
	print x, 