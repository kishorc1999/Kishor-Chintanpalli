import re
a=raw_input("Enter a String:-")
if (re.search('good\s{3}boy',a)):	#"\s{3}" three speces
	print 'found'				
else:
	print 'not found'