from gc import disable
from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0, "Enter a number")  # Placeholder


def clr():
    e.delete(0, END)


def btnClick(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(num))


def add():
    firstnum = e.get()


def subtract():
    pass


def multiply():
    pass


def divide():
    pass


def equals():
    pass


button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: btnClick(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: btnClick(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: btnClick(3)).grid(row=3, column=2)
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: btnClick(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: btnClick(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: btnClick(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: btnClick(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: btnClick(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: btnClick(9)).grid(row=1, column=2)
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: btnClick(0)).grid(row=4, column=0)

addButton = Button(root, text="+", padx=40, pady=20,
                   command=add).grid(row=4, column=1)
subtractButton = Button(root, text="-", padx=40, pady=20,
                        command=subtract).grid(row=4, column=2)
multiplyButton = Button(root, text="*", padx=40, pady=20,
                        command=multiply).grid(row=5, column=1)
divideButton = Button(root, text="/", padx=40, pady=20,
                      command=divide).grid(row=5, column=2)
clrButton = Button(root, text="clr", padx=39, pady=20,
                   command=clr).grid(row=5, column=0)
equalsButton = Button(root, text="=", padx=40,
                      pady=20, command=equals).grid(row=6, column=1)

root.mainloop()
