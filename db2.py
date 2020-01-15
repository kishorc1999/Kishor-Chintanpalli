
'''
2]update:
	update<tablename>
	set colname=value
	where condition
Example:
	update student
	set lname='sharma',rollno=100
	where rollno=2'''
import pymysql
c=pymysql.connect(host='localhost',user='root',passwd='',database='demo')
cur=c.cursor()
cur.execute("update student set fees=fees+1000 where rollno=1")
c.commite()
c.close()