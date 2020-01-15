f1=open('abc.txt','r')
f2=open('pqr.txt','r')
a=f1.read()
b=f2.read()
f1=open('abc.txt','w')
f2=open('pqr.txt','w')
f1.write(b)
f2.write(a)


f1.close()
f2.close()


