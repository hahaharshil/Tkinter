from tkinter import *


def add():
    res = float(e2.get()) + float(e1.get())
    myText.set(res)

def sub():
    res = float(e1.get()) - float(e2.get())
    myText.set(res)

def div():
    res = float(e1.get()) / float(e2.get())
    myText.set(res)

def multi():
    res = float(e1.get()) * float(e2.get())
    myText.set(res)

def clr():
    e1.delete(0, END)
    e2.delete(0, END)




root = Tk()

myText = StringVar()

e1 = Entry(root)
e1.pack()

e2 = Entry(root)
e2.pack()

butt1 = Button(root , text = "Add", command = add)
butt1.pack()

butt2 =  Button(root , text = "Substract" , command = sub)
butt2.pack()

butt3 = Button(root, text = "Divide" , command = div)
butt3.pack()


butt4 = Button(root , text = "Multiply" , command = multi)
butt4.pack()

butt5 = Button(root, text = "Clear" , command = clr)
butt5.pack()

result=Label(root, text="", textvariable=myText)
result.pack()

lbl = Label(root , text = "Oct 10 2020 / creatd by Harshil")
lbl.pack(side = BOTTOM)


root.mainloop()
