import re
a=raw_input("Enter a String:-")
if (re.search('goodboy',a)):
	print 'found'
else:
	print 'not found'