from tkinter import *

root = Tk() #membuat root, window utama
root.title('Toplevel') #mengatur judul root

f = Frame(root, width=300, height=110, relief=SOLID, borderwidth=2)
xf = Frame(f, relief=GROOVE, borderwidth=2) #frame di dalam frame?
Label(xf, text="You shot him!").pack(pady=10)
Button(xf, text="He's dead!", state=DISABLED).pack(side=LEFT, padx=5, pady=8)
Button(xf, text="He's completely dead!", command=root.quit).pack(side=RIGHT, padx=5, pady=8)
xf.place(relx=0.01, rely=0.125, anchor=NW)
Label(f, text='Self-defence against fruit').place(relx=.06, rely=0.125, anchor=W)
f.pack()


