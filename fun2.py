def prime(n):
	flag=0
	for i in range (2,n):
		if n%i==0:
			flag=1
			break
	if flag==1:
		print n,"is composit"
	else:
		print n,"is prime"


num=input("Enter a Number:-")
prime(num)