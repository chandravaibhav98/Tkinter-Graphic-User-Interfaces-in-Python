from msilib.schema import RadioButton
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio_Buttons')
root.iconbitmap('./icons/codemy.ico')

r = IntVar()
r.set(1)

TOPPINGS = [
    ("Cheesy", "Cheesy"),
    ("Pepperoni", "Pepperoni"),
    ("Mushroom", "Mushroom"),
    ("Dominator", "Dominator"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, TOPPING in TOPPINGS:
    Radiobutton(root, variable=pizza, value=TOPPING, text=text).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1,
#             command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 1", variable=r, value=2,
#             command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text='Click', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
