"""function with paramerer and return valu"""
def factorial(num):
	f=1
	for i in range (1,num+1):
		f=f*i
	return f

n=input("Enter a number")
result=factorial(n)
print result