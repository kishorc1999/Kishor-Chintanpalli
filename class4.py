#Constructor:-It is Special Member functon which gets automatically call 
#when the Object is created.
class student:
	def __init__(self):		#default constructor
		self.id=1
		self.name="kishor"
	def display(self):
		print(self.id,self.name)
ob=student()
ob.display()