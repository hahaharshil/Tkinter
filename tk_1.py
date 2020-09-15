 from tkinter import *



root = Tk()
def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")


bt0 = Button(root , text = "Click")
bt0.bind("<Button-1>" , leftClick)
bt0.bind("<Button-2>" , middleClick)
bt0.bind("<Button-3>" , rightClick)
bt0.pack()






root.mainloop()
