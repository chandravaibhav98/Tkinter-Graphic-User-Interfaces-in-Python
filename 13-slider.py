from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('File Dialog')
root.iconbitmap('./icons/codemy.ico')
root.geometry("500x500")


def slide(value):
    horizontal_label = Label(
        root, text=f'Horizontal:{horizontal.get()}').pack()
    vertical_label = Label(root, text=f'Vertical:{vertical.get()}').pack()


vertical = Scale(root, from_=0, to=100)
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=slide)
horizontal.pack()

# horizontal_label = Label(root, text=horizontal.get()).pack()
# vertical_label = Label(root, text=vertical.get()).pack()


my_btn = Button(root, text="Click", command=slide).pack()

root.mainloop()
