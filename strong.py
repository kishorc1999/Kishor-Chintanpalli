n=input("Enter a number")
num=n
sum=0
while n>0:
	rem=n%10
	f=1
	for i in range (1,rem+1):
		f=f*i
	sum=sum+f
	n=n/10

if sum==num:
	print num,"is strong"
else:
	print num,"is not a strong\n"
