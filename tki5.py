from tkinter import *
root=Tk()
root.geometry("800x400")
root.title("Demo Title")
label1=Label(root,text="Demo Label")
label2=Label(root,text="Another Label")
label1.grid(row=0,column=0)
label2.grid(row=5,column=5)
root.mainloop()