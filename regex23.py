import re
x=raw_input('Enter a string')
y=re.compile('boy')
y=y.sub('batsman',x)
print y