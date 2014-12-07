from tkinter import *
import Pmw

def inisialisasi():
    #Code tetap, inisialisasi
    root = Tk()
    root.title('ElGamal Cryptosystem')
    Pmw.initialise()
    # Create and pack the NoteBook.
    notebook = Pmw.NoteBook(root) #membuat objek notebook
    notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
    return notebook
    #========================

def bookgenkey(notebook):
    pageGenkey = notebook.add('Generate Key')

    # Membuat grup yang berisi content page, parent nya page di pageGenKey
    group1 = Pmw.Group(pageGenkey, tag_pyclass=None)

    # Frame 1 - baris 1.
    frame = Frame(group1.interior())

    Label(frame, text='Panjang kunci: ').pack(padx=5, pady=5, side=LEFT)

    listpanjangkey = (4,5,6,7,8,9,10,11,12,13,14,15,16)
    cbpjkey = Pmw.ComboBox(frame,
                           dropdown=1,
                           scrolledlist_items=listpanjangkey)
    cbpjkey.pack(fill='both', padx=5, pady=5, side=LEFT)
    cbpjkey.selectitem(0)

    btngenerate = Button(frame, text="Generate!")
    btngenerate.pack(side=LEFT, padx=5, pady=5)

    frame.pack(fill=BOTH)

    # Frame 2 - baris 2
    frame = Frame(group1.interior())

    Label(frame, text='Lama Waktu Pembangkitan Kunci: ').pack(padx=5, pady=5)

    frame.pack(side=LEFT)

    group1.pack(fill=BOTH, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.

    # Membuat grup yang berisi content page, parent nya page pageGenkey
    group2 = Pmw.Group(pageGenkey, tag_text='Kunci Publik')
    frameluar = Frame(group2.interior())

    frame = Frame(frameluar)
    Label(frame, text='p ').pack(side=LEFT, padx=5, pady=5)
    p = Entry(frame).pack(side=LEFT, expand=1, fill=X, padx=10)
    frame.pack(fill=X, expand=1)

    frame = Frame(frameluar)
    Label(frame, text='a ').pack(side=LEFT, padx=5, pady=5)
    a = Entry(frame).pack(side=LEFT, expand=1, fill=X, padx=10)
    frame.pack(fill=X, expand=1)

    frame = Frame(frameluar)
    Label(frame, text='b ').pack(side=LEFT, padx=5, pady=5)
    b = Entry(frame).pack(side=LEFT, expand=1, fill=X, padx=10)
    frame.pack(fill=X, expand=1)

    frame = Frame(frameluar)
    btnexportpubk = Button(frame, text="Export")
    btnexportpubk.pack(side=LEFT, padx=5, pady=5)
    frame.pack()

    frameluar.pack(fill=X)
    group2.pack(side = LEFT, expand=1, fill=BOTH, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.

    # Membuat grup yang berisi content page, parent nya page pageGenkey
    group3 = Pmw.Group(pageGenkey, tag_text='Kunci Privat')
    frameluar = Frame(group3.interior())

    frame = Frame(frameluar)
    Label(frame, text='p ').pack(padx=5, pady=5, side=LEFT)
    p = Entry(frame, width=25).pack(side=LEFT, expand=1, fill=X, padx=10)
    frame.pack(fill=X, expand=1)

    frame = Frame(frameluar)
    Label(frame, text='d ').pack(padx=5, pady=5, side=LEFT)
    d = Entry(frame, width=25).pack(side=LEFT, expand=1, fill=X, padx=10)
    frame.pack(fill=X, expand=1)

    frame = Frame(frameluar)
    btnexportprivk = Button(frame, text="Export")
    btnexportprivk.pack(side=LEFT, padx=5, pady=5)
    frame.pack()

    frameluar.pack(fill=X)
    group3.pack(side=LEFT, expand=1, fill=BOTH, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.
    
    notebook.setnaturalsize()
    return notebook

def bookenkripsi(notebook):
    pageEnkripsi = notebook.add('Enkripsi')

    # Membuat grup yang berisi content page, parent nya page pageGenkey
    groupKey = Pmw.Group(pageEnkripsi, tag_text='Kunci Publik')

    frame = Frame(groupKey.interior())
    btnexportpubk = Button(frame, text="Import")
    btnexportpubk.pack(side=LEFT, padx=5, pady=5)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupKey.interior())
    Label(frame, text='p ').pack(padx=5, pady=5, side=LEFT)
    p = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupKey.interior())
    Label(frame, text='a ').pack(padx=5, pady=5, side=LEFT)
    a = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupKey.interior())
    Label(frame, text='b ').pack(padx=5, pady=5, side=LEFT)
    b = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    groupKey.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.

    # Membuat grup yang berisi content page, parent nya page pageEnkripsi
    groupPT = Pmw.Group(pageEnkripsi, tag_text='Pesan')

    frame = Frame(groupPT.interior())
    btnexportpubk = Button(frame, text="Import")
    btnexportpubk.pack(side=LEFT, padx=5, pady=5)
    frame.pack(fill=BOTH, padx=5, pady=5)
    
    frame = Frame(groupPT.interior())
    
    textPesan = Text(frame, height=4)
    scrollTp = Scrollbar(frame, command=textPesan.yview)
    textPesan.configure(yscrollcommand=scrollTp.set)
    textPesan.pack(side=LEFT, fill=BOTH, expand=1)
    scrollTp.pack(side=LEFT, fill=Y)
    
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

    frame = Frame(groupPT.interior())
    btnexportpubk = Button(frame, text="Enkripsi")
    btnexportpubk.pack(padx=5, pady=5)
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

    groupPT.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.

    # ------------
    groupCT = Pmw.Group(pageEnkripsi, tag_text='Cipher Text')
    
    # ============
    frame = Frame(groupCT.interior())

    frame1 = Frame(frame)
    Label(frame1, text='Ciphertext 1').pack(padx=5, pady=5, side=LEFT)
    frame1.pack(fill=X, padx = 5, pady = 5)
    
    frame1 = Frame(frame)
    textC1 = Text(frame1, height=4)
    scrollC1 = Scrollbar(frame1, command=textC1.yview)
    textC1.configure(yscrollcommand=scrollC1.set)
    textC1.pack(fill=BOTH, side=LEFT, expand=1)
    scrollC1.pack(side=LEFT, fill=Y)
    frame1.pack(fill=X, expand=1, padx = 5, pady = 5)
    
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

    # ============
    frame = Frame(groupCT.interior())

    frame1 = Frame(frame)
    Label(frame1, text='Ciphertext 2').pack(padx=5, pady=5, side=LEFT)
    frame1.pack(fill=X, padx = 5, pady = 5)
    
    frame1 = Frame(frame)
    textC2 = Text(frame1, height=4)
    scrollC2 = Scrollbar(frame1, command=textC2.yview)
    textC2.configure(yscrollcommand=scrollC1.set)
    textC2.pack(fill=BOTH, side=LEFT, expand=1)
    scrollC2.pack(side=LEFT, fill=Y)
    frame1.pack(fill = X, expand=1, padx = 5, pady = 5)
    
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

    framebtn = Frame(groupCT.interior())
    btnexportC2 = Button(framebtn, text="Eksport")
    btnexportC2.pack(padx=5, pady=5)
    framebtn.pack(fill=X)
    
    # -------------------
    groupCT.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.
    
    notebook.setnaturalsize()
    return notebook

def bookdekripsi(notebook):
    pageDekripsi = notebook.add('Dekripsi')

    # Membuat grup yang berisi content page, parent nya page pageGenkey
    group1 = Pmw.Group(pageDekripsi, tag_text='Kunci Privat')

    frame = Frame(group1.interior())
    btnexportpubk = Button(frame, text="Import")
    btnexportpubk.pack(side=LEFT, padx=5, pady=5)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(group1.interior())    
    Label(frame, text='p ').pack(padx=5, pady=5, side=LEFT)
    p = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(group1.interior())
    Label(frame, text='d ').pack(padx=5, pady=5, side=LEFT)
    d = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    group1.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.

    # Membuat grup yang berisi content page, parent nya page pageEnkripsi
    group2 = Pmw.Group(pageDekripsi, tag_text='Ciphertext')

    framebtn = Frame(group2.interior())
    btnexportC1 = Button(framebtn, text="Import")
    btnexportC1.pack(side=LEFT, padx=10, pady=5)
    framebtn.pack(fill=X)
    
    # ============
    frame = Frame(group2.interior())

    frame1 = Frame(frame)
    Label(frame1, text='Ciphertext 1').pack(padx=5, pady=5, side=LEFT)
    frame1.pack(fill=X, padx = 5, pady = 5)
    
    frame1 = Frame(frame)
    textC1 = Text(frame1, height=4)
    scrollC1 = Scrollbar(frame1, command=textC1.yview)
    textC1.configure(yscrollcommand=scrollC1.set)
    textC1.pack(fill=BOTH, side=LEFT, expand=1)
    scrollC1.pack(side=LEFT, fill=Y)
    frame1.pack(fill=X, expand=1, padx = 5, pady = 5)
    
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

    # ============
    frame = Frame(group2.interior())

    frame1 = Frame(frame)
    Label(frame1, text='Ciphertext 1').pack(padx=5, pady=5, side=LEFT)
    frame1.pack(fill=X, padx = 5, pady = 5)

    frame1 = Frame(frame)
    textC2 = Text(frame1, height=4)
    scrollC2 = Scrollbar(frame1, command=textC2.yview)
    textC2.configure(yscrollcommand=scrollC1.set)
    textC2.pack(fill=BOTH, side=LEFT, expand=1)
    scrollC2.pack(side=LEFT, fill=Y)
    frame1.pack(fill = X, expand=1, padx = 5, pady = 5)
    
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

    frame = Frame(group2.interior())
    btnexportpubk = Button(frame, text="Dekripsi")
    btnexportpubk.pack(padx=5, pady=5)
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
    
    group2.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.
    
    # ===========
    groupPT = Pmw.Group(pageDekripsi, tag_text='Plaintext')
    
    frame = Frame(groupPT.interior())
    
    textPesan = Text(frame, height=4)
    scrollTp = Scrollbar(frame, command=textPesan.yview)
    textPesan.configure(yscrollcommand=scrollTp.set)
    textPesan.pack(side=LEFT, fill=BOTH, expand=1)
    scrollTp.pack(side=LEFT, fill=Y)
    
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

    frame = Frame(groupPT.interior())
    btnexportPT = Button(frame, text="Eksport")
    btnexportPT.pack(padx=5, pady=5)
    frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
    
    groupPT.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.
    
    notebook.setnaturalsize()
    return notebook

def bookHack(notebook):
    pageHack = notebook.add('Hack')

    # Membuat grup yang berisi content page, parent nya page pageGenkey
    groupPubKey = Pmw.Group(pageHack, tag_text='Kunci Publik')

    frame = Frame(groupPubKey.interior())
    btnexportpubk = Button(frame, text="Import")
    btnexportpubk.pack(side=LEFT, padx=5, pady=5)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupPubKey.interior())
    Label(frame, text='p ').pack(padx=5, pady=5, side=LEFT)
    p = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupPubKey.interior())
    Label(frame, text='a ').pack(padx=5, pady=5, side=LEFT)
    a = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupPubKey.interior())
    Label(frame, text='b ').pack(padx=5, pady=5, side=LEFT)
    b = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    groupPubKey.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.

    # Membuat grup yang berisi content page, parent nya page pageGenkey
    groupPrivKey = Pmw.Group(pageHack, tag_text='Kunci Privat')

    frame = Frame(groupPrivKey.interior())
    btnexportpubk = Button(frame, text="Eksport")
    btnexportpubk.pack(side=LEFT, padx=5, pady=5)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupPrivKey.interior())    
    Label(frame, text='p ').pack(padx=5, pady=5, side=LEFT)
    p = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    frame = Frame(groupPrivKey.interior())
    Label(frame, text='d ').pack(padx=5, pady=5, side=LEFT)
    d = Entry(frame, width=25).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)

    groupPrivKey.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.

    # Membuat grup yang berisi content page, parent nya page pageGenkey
    groupTime = Pmw.Group(pageHack, tag_pyclass=None)
    
    frame = Frame(groupTime.interior())    
    Label(frame, text='Panjang Kunci: ').pack(padx=5, pady=5, side=LEFT)
    lvlpjkey = Label(frame, text='-').pack(padx=5, pady=5, side=LEFT)
    frame.pack(fill = X, padx=5, pady=5)

    frame = Frame(groupTime.interior())    
    Label(frame, text='Waktu Pemecahan Kunci: ').pack(padx=5, pady=5, side=LEFT)
    lvltimehack = Label(frame, text='-').pack(padx=5, pady=5, side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)
    
    groupTime.pack(fill=X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # packing grup.
    
    notebook.setnaturalsize()
    return notebook

notebook = inisialisasi()
bookgenkey(notebook)
bookenkripsi(notebook)
bookdekripsi(notebook)
bookHack(notebook)
