f=open('abc.txt','r')
lcnt=0
tcnt=0
scnt=0
ccnt=0
ch=f.read(1)
while len(ch)>0:
	if (ch=='\n'):
		lcnt=lcnt+1
	if (ch==' '):
		scnt=scnt+1
	if (ch=='\t'):
		tcnt=tcnt+1
	ccnt=ccnt+1
	ch=f.read(1)

print 'number of lines ',lcnt
print 'number of spaces ',scnt
print 'number of tabs ',tcnt
print 'number of characters ',ccnt