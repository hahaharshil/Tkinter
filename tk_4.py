from tkinter import *


def mn():
    a = ent.get()
    b = entx.get()
    ab = int(a) + int(b)
    t3.insert(END, str(result))

def nb():

    a = ent.get()
    b = entx.get()
    ab = int(a) - int(b)

    t3.insert(END, str(result))





root = Tk()

ll = Label(root, text = "result")
ll.pack()

t3 = Entry(root)
t3.pack()


mask = Frame(root)

ent = Entry(mask, text = "Number")
ent.pack()
entx = Entry(mask, text = "Number1")
entx.pack()


butt = Button(mask, text = "Add" , command = mn)
butt.pack(side = LEFT)


buttt = Button(mask, text = "Substract" , command = nb)
buttt.pack(side = RIGHT)






mask.pack()

root.mainloop()
