import sqlite3
conn=sqlite3.connect("Doctor.db")
with conn:
	cur=conn.cursor()
	cur.execute("SELECT * FROM Doctor")

	for row in cur.fetchall():
		print("ID ::"+str(row[0]))
		print("name ::"+row[1])
		print("qual ::"+row[2])
		print("spec ::"+row[3])


