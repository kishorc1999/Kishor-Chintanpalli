f1=open('abc.txt','r')
f2=open('pqr.txt','w')
s=f1.read()
print s
i=len(s)-1
r=''
while i>=0:
	r = r + s[i]
	print r
	i=i-1
#r=s[::-1]      another way

print r
f2.write(r)
f1.close()
f2.close()


