def demo():
	try:
		a=input('Enter number1:-')
		b=input('\nEnter number2:-')
		c=a/b
		print 'division is',c
		return
	except:
		print 'Exception occured'
	finally:
		print 'Exception program'
demo()