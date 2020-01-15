import re
a=raw_input("Enter a String:-")
if (re.search('is\s*\w+ good',a)):	
	print 'found'				
else:
	print 'not found'