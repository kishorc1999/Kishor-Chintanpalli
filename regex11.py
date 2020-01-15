import re
a=raw_input("Enter a String:-")
if (re.search('is\s*\d{1,}',a)):	#\d=numeric value
	print 'found'				
else:
	print 'not found'