from tkinter import *
top = Tk()
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
# Code to add widgets will go here...
B = Button(top, text ="Hello", command=helloCallBack)
B.pack()
top.mainloop()
