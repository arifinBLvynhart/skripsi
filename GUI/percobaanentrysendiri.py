from tkinter import *

root = Tk() #membuat root, window utama
root.title('Toplevel') #mengatur judul root

Label(root, text="Anagram:").pack(side=TOP, padx=5, pady=10)
e = StringVar() #membuat sebuah variabel string? ;angsung singkron semua?
f = Frame(root)
e1 = Entry(f, width=40, textvariable=e).pack(side=LEFT)
f.pack(side=TOP, expand=YES, fill=BOTH)

f2 = Frame(root)
Entry(f2, width=40, textvariable=e).pack(side=LEFT)
f2.pack(side=TOP, expand=YES, fill=BOTH)

var = IntVar()
for text, value in [('Passion fruit', 1), ('Loganberries', 2),
                    ('Mangoes in syrup', 3), ('Oranges', 4),
                    ('Apples', 5),('Grapefruit', 6)]:
    Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
var.set(3)
