import re
a=raw_input("Enter a String:-")
if (re.search('good\s{1,}boy',a)):	#"\s{1,}" minimum one speace 
	print 'found'				
else:
	print 'not found'