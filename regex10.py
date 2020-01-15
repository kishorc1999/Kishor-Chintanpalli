import re
a=raw_input("Enter a String:-")
if (re.search('good\s{1,4}boy',a)):	#"\s{1,4}" minimum one maximum four speaces
	print 'found'				
else:
	print 'not found'