'''
1]Insert:
	insert into<tablename>[fieldlist]values(val1,val2,.......,valn)


Example:
	1]insert into student values(1,'virat','kholi')
	2]insert into student (rollno,fname) values(2,'rohit')
	3]insert into student (fname,lname,rollno) values('shiker','dhavan',3)
	'''

import pymysql
c=pymysql.connect(host='localhost',user='root',passwd='',database='demo')
cur=c.cursor()
cur.execute("insert into student values(1,'jasprit',bumrah)")
c.commite()
c.close()
