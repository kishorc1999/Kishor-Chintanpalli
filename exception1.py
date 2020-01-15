#the abnormal termination of a computer program is known as Exception
try:
	a=input('\nEnter number1:-')
	b=input('\nEnter number2:-')
	c=a/b
	print 'Division is:-',c
except(ZeroDivisionError):
	print 'Denominator can not be zero'
except(NameError):
	print 'only integer allowed'
print 'Exception program'