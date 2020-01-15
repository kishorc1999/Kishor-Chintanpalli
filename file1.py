#it is collection of records stored on secondary device .
#the purpose of file in any language is to provide persistency(permenant storage)
'''r=read only(BOF)
   w=write and if file does not exist it will create new file(BOF)
   a=write and create(EOF)
   r+=read and write(BOF)
   w+=write ,read and if file does not exist it will createe file(BOF)
   a+=write ,read and if file does not exist it will createe file(EOF)'''
a=open('abc.txt','r')
b=a.read()
print b
