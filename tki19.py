import sqlite3
conn=sqlite3.connect("Doctor.db")
with conn:
	cur=conn.cursor()
	cur.execute("insert into Doctor(name,qual,spec) values('Kedar','BE','CSE')")
	print("Record Inserted")