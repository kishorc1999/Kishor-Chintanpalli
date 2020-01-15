from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("RadioButton")
root.geometry("200x200")
rbstr=StringVar()
def disp():
	print("you selected "+rbstr.get())
rb1=Radiobutton(root,text="Male",variable=rbstr,value="male",command=disp)
rb2=Radiobutton(root,text="Female",variable=rbstr,value="female",command=disp)
btn1=Button(root,text="Add",Command=disp)
rb1.pack()
rb2.pack()
btn1.place(x=30,y=80)
root.mainloop()