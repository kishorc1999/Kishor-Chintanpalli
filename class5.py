class student:
	def __init__(self,a,b):		#parameterized constructor
		self.id=a
		self.name=b
	def display(self):
		print(self.id,self.name)
ob=student(1,"kishor")
ob.display()