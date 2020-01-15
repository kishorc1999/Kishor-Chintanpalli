import re
a=raw_input("Enter a String:-")
if (re.search('good.boy',a)):	# '.' any charecter example:-" ",",","a","1"
	print 'found'				# single in number
else:
	print 'not found'