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
		root.destroy()
		dash=Tk()
		dash.title("Dashbord")
		dash.geometry("1200x800")
		label=Label(dash,text="Doctor")
		label.pack()
		label4=Label(dash,text="Name")
		label5=Label(dash,text="Qaulification")
		label6=Label(dash,text="Specialization")
		entry4=Entry(dash)
		entry5=Entry(dash)
		entry6=Entry(dash)
		label4.place(x=500,y=70)
		entry4.place(x=600,y=70)
		label5.place(x=500,y=130)
		entry5.place(x=600,y=130)
		label6.place(x=500,y=190)
		entry6.place(x=600,y=190)
		def sub():
			print(""+"\n"+entry4.get()+"\n"+entry5.get()+"\n"+entry6.get())
			msg=messagebox.showinfo("Submit Status","Successfull")
		def clr():
			entry4.delete(0,END)
			entry5.delete(0,END)
			entry6.delete(0,END)
		btn3=Button(dash,text="Submit",command=sub)
		btn3.place(x=530,y=250)
		btn4=Button(dash,text="clear",command=clr)
		btn4.place(x=620,y=250)
		dash.mainloop()

	else:
		msg=messagebox.showinfo("Login Status","Login Failed")


btn1=Button(root,text="Login",command=login)
btn1.place(x=160,y=180)
btn2=Button(root,text="clear",command=clr)
btn2.place(x=250,y=180)
root.mainloop()