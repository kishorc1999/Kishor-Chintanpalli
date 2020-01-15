import re
x=raw_input('Enter a string:-')
if(re.search('Good',x,re.I)):     #'I':- ignore case
	print 'found'
else:
	print 'not found'