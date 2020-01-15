import sqlite3
conn=sqlite3.connect("Doctor.db")
with conn:
	cur=conn.cursor()
	cur.execute("UPDATE Doctor set name='Kishor Chintanpalli' where id='9'")
	print("Record Inserted")