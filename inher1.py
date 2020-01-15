#inheritance:-Ability of one class to acquire properties of another class is known as inheritance.
class A:
	def fun1(self):
		print("In A")		#single inheritance
class B(A):
	def fun2(self):
		print ("In B")
ob=B()
ob.fun1()
ob.fun2()