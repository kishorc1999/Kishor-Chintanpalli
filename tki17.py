from tkinter import *
from tkinter import ttk
import sqlite3
root=Tk()
root.title("Login page")
root.geometry("300x300")
treeV=ttk.Treeview(root,selectmode="extended",columns=('id','name','qual','spec'))
treeV.heading('#0',text="",anchor=CENTER)
treeV.heading('#1',text="id",anchor=CENTER)
treeV.heading('#2',text="name",anchor=CENTER)
treeV.heading('#3',text="qual",anchor=CENTER)
treeV.heading('#4',text="spec",anchor=CENTER)
treeV.column('#0',width=20)
treeV.column('#1',width=100)
treeV.column('#2',width=100)
treeV.column('#3',width=100)
treeV.column('#4',width=100)
treeV.pack()
conn=sqlite3.connect("Doctor.db")
with conn:
	cur=conn.cursor()
	cur.execute("SELECT * FROM Doctor")
	for row in cur.fetchall():
		treeV.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3]))
		

root.mainloop()