from tkinter import *
root=Tk()
root.geometry("800x400")
root.title("Demo Title")
label1=Label(root,text="Name")			
label2=Label(root,text="Password")
entry1=Entry(root)					### Text Box
entry2=Entry(root,show="*")			### Text For Password
label1.place(x=30,y=20)
entry1.place(x=100,y=20)
label2.place(x=30,y=60)
entry2.place(x=100,y=60)
def disp():
	print(""+entry1.get()+entry2.get())

btn1=Button(root,text="click Me",Command=disp)
btn1.place(x=50,y=80)

root.mainloop()