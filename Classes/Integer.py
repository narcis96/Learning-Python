class Integer:
	count = 0
	def __init__(self, y):
		self.__x = y #private
		Integer.count += 1
	def Set(self,y):
		self.k = self.__x #public
		self.__x =  y
	def Get(self):
		return self.__x
		
def my_generator(left, right):
	while (left <= right):
		yield Integer(left)
		left += 1

list = [x for x in my_generator(1,10)]
for x in list:
	x.Set(x.Get()*x.Get())
for x in list:
	print x.k,
	print x.Get()
print 'server is up'
for i in xrange(1,10):
	print '.',
	
print "Number of integers created is %d" %Integer.count

