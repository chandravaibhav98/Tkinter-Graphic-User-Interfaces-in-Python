from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('DropDown Menu')
root.iconbitmap('./icons/codemy.ico')
root.geometry("200x200")


clicked = StringVar()
clicked.set("Sunday")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = ["Monday", "Tuesday",
           "Wednesday", "Thursday", "Friday", "Saturday"]

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
