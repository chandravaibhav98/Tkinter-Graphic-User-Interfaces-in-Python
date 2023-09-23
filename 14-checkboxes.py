from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Checkboxes')
root.iconbitmap('./icons/codemy.ico')
root.geometry("200x200")


def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="SuperSize? RegularSize",
                variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
