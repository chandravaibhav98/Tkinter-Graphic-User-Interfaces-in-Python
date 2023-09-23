from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Create new Windows')
root.iconbitmap('./icons/codemy.ico')


def openWindow():
    top = Toplevel()
    top.title('Create new Windows')
    top.iconbitmap('./icons/codemy.ico')
    global my_img
    my_img = ImageTk.PhotoImage(Image.open('./images/python-tkinter.jpg'))
    my_label = Label(top, image=my_img).pack()
    closeWindowBtn = Button(top, text='Exit', command=top.destroy).pack()


openWindowBtn = Button(root, text='Open Window', command=openWindow).pack()

root.mainloop()
