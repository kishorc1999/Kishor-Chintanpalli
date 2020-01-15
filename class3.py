class student:
	def setValue(self,a,b):
		self.id=a
		self.name=b
	def display(self):
		print(self.id,self.name)

ob=student()
x=int(input("Enter Roll Number ::"))
y=input("Enter Name ::")
ob.setValue(x,y)
ob.display()