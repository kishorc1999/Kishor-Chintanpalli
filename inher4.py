#herarchicle
class A:
	def fun1(self):
		print("In A")

class B(A):
	def fun2(self):
		print("In B")	

class C(A):
	def fun3(self):
		print("In C")
ob=B()
ob=C()
ob.fun1()
ob.fun2()
ob.fun3()