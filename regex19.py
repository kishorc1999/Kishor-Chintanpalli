import re
a=raw_input("Enter a String:-")
if (re.search('is [a-g][^a-g]od',a)):	# [^a-g] other than a to g	
	print 'found'						#also numeric values are allowed
else:									#special charecters are allowed
	print 'not found'