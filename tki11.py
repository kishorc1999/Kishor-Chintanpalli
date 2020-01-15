from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("RadioButton")
root.geometry("200x200")
rbstr=StringVar()
def disp():
	#print("you selected "+rbstr.get())
	lb1=Label(root,text=rbstr.get())
	#lb1.pack()
	lb1.place(x=120,y=120)
rb1=Radiobutton(root,text="Male  ",variable=rbstr,value="male   ")
rb2=Radiobutton(root,text="Female",variable=rbstr,value="female")
btn1=Button(root,text="Add",command=disp)
rb1.place(x=20,y=40)
rb2.place(x=20,y=80)
btn1.place(x=20,y=120)

root.mainloop()