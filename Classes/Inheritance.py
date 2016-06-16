class BaseClassName:
	
	def __init__(self, x):
		self.x = x
	def Print(self):
		print self.x

class DerivedClassName(BaseClassName):	
	def __init__(self, y):
		self.y = y
	def Print(self):
		print self.y, x
		
obj1 = BaseClassName(1)
obj2 = DerivedClassName(3)


obj1.Print()
obj2.Print()