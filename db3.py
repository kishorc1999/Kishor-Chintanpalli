'''
3] delete:
	delete from <tablename>
	where condition

Example:
	delete from student
	where rollno=3
'''

import pymysql
c=pymysql.connect(host='localhost',user='root',passwd='',database='demo')
cur=c.cursor()
cur.execute("delete from student where rollno=3")
c.commite()
c.close()