#ini adalah contoh penggunaan top level widget
from tkinter import *

root = Tk() #membuat root, window utama
root.title('Toplevel') #mengatur judul root
Label(root, text='This is the main (default) Toplevel').pack(pady=10) #membuat sebuah label

t1 = Toplevel(root) #membuat sebuah toplevel, dengan parent root.
Label(t1, text='This is a child of root').pack(padx=10, pady=10) #membuat sebuah label

t2 = Toplevel(root) #membuat sebuah top level lain dengan parent root.
Label(t2, text='This is a transient window of root').pack(padx=10, pady=10)
t2.transient(root) #membuatnya menjadi transient, selalu di atas root, dan akan hidden jika root di-minimize

t3 = Toplevel(root, borderwidth=5, bg='blue') #membuat toplevel / container lain
Label(t3, text='No wm decorations', bg='blue', fg='white').pack(padx=10, pady=10) #membuat label
t3.overrideredirect(1) #menghilangkan tombol minimize, maximize, dan close, juga judul window dan border.
t3.geometry('400x370+150+350') #mengatur geometri? 'panjangxlebar+koordinatxlayar,koordinatylayar'

root.mainloop()
