import re
a=raw_input("Enter a String:-")
if (re.search('good\s*boy',a)):	#"\s*" single or multiple speaces allowed
	print 'found'				#no space is also allowed
else:
	print 'not found'