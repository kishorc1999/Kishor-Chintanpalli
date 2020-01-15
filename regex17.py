import re
a=raw_input("Enter a String:-")
if (re.search('is [a-g]ood boy',a)):	#[a-g] a to g charecters are allowed
	print 'found'				
else:
	print 'not found'