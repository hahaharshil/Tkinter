from tkinter import *
class win:

    def __init__(self):

        self.ent1 = Entry(root)
        self.ent1.pack()
        self.ent2 = Entry(root)
        self.ent2.pack()
        self.mnmn = self.ent1.get()
        self.hms = self.ent2.get()
        self.butt = Button(root , text = "Add" , command = self.add)
        self.butt.pack(side = BOTTOM)
        self.butt2 = Button(root , text = "Substract")
        self.butt2.pack(side = BOTTOM)
        self.clr = Button(root, text = "Clear")
        self.clr.pack(side = BOTTOM)
    
    def sub(self):
        self.y = int(self.mnmn) - int(self.hms)
        self.entr = Entry(root)
        self.entr.pack()
        self.entr.delete(0, END)
        self.entr.insert(0, str(self.y)


    
    
root = Tk()

h = win()
h.nott()


root.mainloop()
