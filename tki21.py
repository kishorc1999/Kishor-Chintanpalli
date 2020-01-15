import sqlite3
conn=sqlite3.connect("Doctor.db")
with conn:
	cur=conn.cursor()
	cur.execute("DELETE from Doctor where id='7'")
	print("Record Deleted")