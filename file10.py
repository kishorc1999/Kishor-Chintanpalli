f1=open('abc.txt','r')
f2=open('pqr.txt','r')
f3=open('xyz.txt','w')
s1=""
ch=f1.read(1)
while len(ch) > 0:
	s1=s1+ch
	ch=f1.read(1)
s2=""
ch=f2.read(1)
while len(ch) > 0:
	s2=s2+ch
	ch=f2.read(1)	
s3=s1+s2
f3.write(s3)	