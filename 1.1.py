from tkinter import *
import os


def get():
    name = ent.get()
    passw = ent1.get()
    result = int(name) + int(passw)
    
    entr = Entry(root)
    entr.delete(0 , "end")
    entr.pack(side = BOTTOM)
    entr.insert(END , str(result))
    

 




root = Tk()


butt = Button(root , text = "Hi" , bg = "#c40e90" , activebackground = "#123456" , command = get)
butt.pack(side = BOTTOM)


ent = Entry(root)
ent.pack()

ent1 = Entry(root)
ent1.pack()













root.mainloop()











