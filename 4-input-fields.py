from gc import disable
from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")  # Placeholder


def button1Click():
    hello = "Hi " + e.get()  # .get() input
    clickedLabel = Label(root, text=hello)
    clickedLabel.pack()


button1 = Button(root, text="Click here", padx=10,
                 pady=10, command=button1Click)
button1.pack()

root.mainloop()
