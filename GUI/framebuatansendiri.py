from tkinter import *

root = Tk() #membuat root, window utama
root.title('Toplevel') #mengatur judul root

f = Frame(root, width=300, height=110)
Label(f, text="You shot him!").pack(pady=10)
Button(f, text="He's dead!", state=DISABLED).pack(side=LEFT, padx=5, pady=8)
Button(f, text="He's completely dead!", command=root.quit).pack(side=RIGHT, padx=5, pady=8)
f.pack()
