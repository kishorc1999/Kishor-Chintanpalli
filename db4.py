'''
4]Select:
	select colname1,.....,colnamen
	from <tablename>
	where condition
Example:
	select fname,lname
	from student
	where rollno=1
'''

import mysql.connector
c=mysql.connector connect(host='localhost',user='root',passwd='',database='demo')
cur=c.cursor()
x=cur.rxecute("select * from student")
p=cur.fetchall()	#fetchone
fot i in p:
	print i
c.close()