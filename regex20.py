import re
a=raw_input("Enter a String:-")
x = (re.findall('is\s*is ',a))
print len(x)
	