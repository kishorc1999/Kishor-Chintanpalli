import re
a=raw_input("Enter a String:-")
if (re.search('is\s*\w*',a)):	
	print 'found'				
else:
	print 'not found'