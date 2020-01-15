from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x400")
root.title("Login Form")
label1=Label(root,text="Name")			
label2=Label(root,text="Password")	
entry1=Entry(root)					
entry2=Entry(root,show="*")	
label1.place(x=100,y=70)
entry1.place(x=200,y=70)
label2.place(x=100,y=130)
entry2.place(x=200,y=130)
					
def clr():
	entry1.delete(0,END)
	entry2.delete(0,END)

def login():
	if entry1.get()=="kishor" and entry2.get()=="kishor":							
		msg=messagebox.showinfo("Login Status","Login Successful")
		root.destroy()
		dash=Tk()
		dash.title("Dashbord")
		dash.geometry("1200x800")
		dash.mainloop()

	else:
		msg=messagebox.showinfo("Login Status","Login Faild")


btn1=Button(root,text="Login",command=login)
btn1.place(x=160,y=180)
btn2=Button(root,text="clear",command=clr)
btn2.place(x=250,y=180)
root.mainloop()