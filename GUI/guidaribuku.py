from tkinter import *

def frame(root, side):  
    w = Frame(root) #membuat frame, parent root
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None): 
    w = Button(root, text=text, command=command) #membuat tombol, parent root
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class Calculator(Frame):
    def __init__(self): #inisialisasi
        Frame.__init__(self) #menginisialisasi frame? atau menjadikan ini frame
        self.pack(expand=YES, fill=BOTH) #meletakkan frame.
        #mengatur title dan icon
        self.master.title('Simple Calculator')
        self.master.iconname("calc1")

        display = StringVar() 
        Entry(self, relief=SUNKEN, 
        textvariable=display).pack(side=TOP, expand=YES,fill=BOTH) #entry, root self
        
        for key in ("123", "456", "789", "-0."): #untuk setiap 3 angka
            keyF = frame(self, TOP) #buat frame, root self
            for char in key: #untuk setiap angka di dalam 3 tadi
                button(keyF, LEFT, char, 
                lambda w=display, s=' %s '%char: w.set(w.get()+s)) #buat button, lambda mungkin mewakili
                                                                   #fungsi yang dipanggil
                                                                   #mengganti nilai display, dengan menambahkan char
                                                                   #baris setelah lambda berarti menggantikan display menjadi w
                                                                   #w.set dan w.get, ya seperti biasa.
        opsF = frame(self, TOP) #frame baru untuk operator.
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char, lambda w=display, c=char: w.set(w.get()+' '+c+' '))
        clearF = frame(self, BOTTOM) #frame baru untuk clear layar
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))

    def calc(self, display):
        #blok try catch
        try:
            display.set(eval(display.get())) #fungsi eval untuk menghitung apa yang tertulis
        except:
            display.set("ERROR")

if __name__ == '__main__':
    Calculator().mainloop()
