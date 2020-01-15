import re
a=raw_input("Enter a String:-")
if (re.search('good.*boy',a)):	#".*" zero,single or multiple speaces allowed
	print 'found'
else:
	print 'not found'