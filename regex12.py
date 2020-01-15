import re
a=raw_input("Enter a String:-")
if (re.search('is\s*\w{1,}',a)):	#\w=alpha and numeric value allowed
	print 'found'				
else:
	print 'not found'