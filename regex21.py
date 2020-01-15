import re
a=open('abc.txt','r')
s=a.read()
p=raw_input('Enter a string')
print p
x=re.findall(p,s)
print len(x)
a.close()