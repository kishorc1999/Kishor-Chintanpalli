f=open('xyz.txt','r')
x=raw_input('Enter a string ')
ch=f.read()

if x in ch:
		print x,' found'
else:
		print x,' not found'
