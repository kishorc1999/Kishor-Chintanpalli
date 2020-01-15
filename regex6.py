import re
a=raw_input("Enter a String:-")
if (re.search('good.+boy',a)):	#".+" single or multiple speaces allowed
	print 'found'				#zero speace not allowes
else:
	print 'not found'