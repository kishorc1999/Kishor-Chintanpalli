import re
a=open('abc.txt','r')
x=a.read()
y=re.compile('boy')
y=y.sub('batsman',x)
a.close()
a=open('abc.txt','w')
a.write(y)
a.close()
print 'task completed'