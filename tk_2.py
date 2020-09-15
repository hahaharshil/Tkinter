from tkinter import *

class myButton:
    def __init__(self):
        self.frame = Frame()
        self.frame.pack()



    def quitButton(self):
        self.quitButton = Button(text = "Quit" , command = self.frame.quit)
        self.quitButton.pack()

class Myselfdow:
    def hs(self):
        self.lbl1=Label(self, text='First number')
        self.lbl2=Label(self, text='Second number')
        self.lbl3=Label(self, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(self, text='Add')
        self.btn2=Button(self, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(self, text='Add', command=self.add)
        self.b2=Button(self, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))
