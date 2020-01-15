from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("Login Form")
label1=Label(root,text="Name")		## Text	
label2=Label(root,text="Password")	
entry1=Entry(root)					### Text Box
entry2=Entry(root,show="*")			### Text For Password
label1.place(x=100,y=70)
entry1.place(x=200,y=70)
label2.place(x=100,y=130)
entry2.place(x=200,y=130)


def disp():								
	print(""+entry1.get()+entry2.get())


def clr():
	entry1.delete(0,END)		##Clear Box
	entry2.delete(0,END)

btn1=Button(root,text="Login",command=disp)		#(Text on Button,function call)
btn1.place(x=160,y=180)
btn2=Button(root,text="clear",command=clr)
btn2.place(x=250,y=180)
root.mainloop()