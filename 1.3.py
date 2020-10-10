from tkinter import *


root = Tk()

def dn():

    ent1 = Entry(root)
    ent1.pack()
    ent2 = Entry(root)
    ent2.pack()
    mnmn = ent1.get()
    hms = ent2.get()
    butt = Button(root , text = "Add")
    butt.pack(side = BOTTOM)
    clr.pack(side = BOTTOM)
    butt2 = Button(root , text = "Substract")
    butt2.pack(side = BOTTOM)
    clr = Button(root, text = "Clear")


def sub():
    y = int(mnmn) - int(hms)
    entr = Entry(root)
    entr.pack()
    entr.delete(0, END)
    entr.insert(0, str(y)




hey = Button(root , text = "hey")
hey.pack()

root.mainloop()