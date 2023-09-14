from gc import disable
from tkinter import *

root = Tk()


def button1Click():
    clickedLabel = Label(root, text="Thanks")
    clickedLabel.pack()


button1 = Button(root, text="Click here", padx=50,
                 pady=50, command=button1Click)
button1.pack()

root.mainloop()
