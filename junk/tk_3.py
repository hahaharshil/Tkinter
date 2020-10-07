from tkinter import *

def dot():
    print("Wow, This works")


root = Tk()

# ********* Menu *********

menu = Menu(root)
root.config(menu = menu)

submenu = Menu(menu)
menu.add_cascade(label = "file" , menu=submenu)
submenu.add_command(label = "New object" , command=dot)
submenu.add_command(label = "New" , command=dot)

submenu.add_separator()
submenu.add_command(label="Exit", command = dot)


editmenu = Menu(menu)
menu.add_cascade(label = "Edit" , menu = editmenu)
menu.add_command(label="redo", command = dot)



# ********* Toolbar *********

toolbar = Frame(root, bg = "blue")

butt = Button(toolbar, text = "Print image" , command=dot)
butt.pack(side = LEFT , padx = 2 , pady = 2)

buttt = Button(toolbar,text = "Print", command =dot)
buttt.pack(side=LEFT, padx = 1 , pady = 1)

butt1 = Button(toolbar, text = "hey" , command = dot)
butt1.pack(side = RIGHT)

toolbar.pack(side = TOP , fill=X)

# end command
root.mainloop()
