#the abnormal termination of a computer program is known as Exception
try:
	a=input('\nEnter number1:-')
	b=input('\nEnter number2:-')
	c=a/b
	print 'Division is:-',c
except:
	print'Exception occured please check input'
print 'Exception program'