try:
	f=open("abc.txt","w")
	ch=raw_input("Enter a string")
	print type(ch)
	f.write(ch)
	f.close()
except:
	print 'error'	