from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Using Icons, Images and Exit Buttons')
root.iconbitmap('./icons/codemy.ico')

button_quit = Button(
    root, text='Exit Program with root.quit()', command=root.quit)
button_quit.pack()

python_img = ImageTk.PhotoImage(Image.open('./images/python.png'))
python_label = Label(image=python_img)
python_label.pack()

root.mainloop()
