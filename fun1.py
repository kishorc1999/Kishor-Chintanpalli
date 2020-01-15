def arm(n):
	sum=0
	while n>0:
		rem=n%10
		sum=sum+(rem*rem*rem)
		n=n/10
	return sum
	


num=input("Enter a number")
s=arm(num)

if s==num:
	print num,"is Armstrong"
else:
	print num,"is not Armstrong "

