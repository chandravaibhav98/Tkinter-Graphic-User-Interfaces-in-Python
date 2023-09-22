from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Using Icons, Images and Exit Buttons')
root.iconbitmap('./icons/codemy.ico')


python_img = ImageTk.PhotoImage(Image.open('./images/python.png'))
python_tkinter_img = ImageTk.PhotoImage(
    Image.open('./images/python-tkinter.jpg'))
python_scikitlearn_img = ImageTk.PhotoImage(
    Image.open('./images/python-sckitlearn.jpeg'))
python_flask_img = ImageTk.PhotoImage(Image.open('./images/python-flask.png'))
python_django_img = ImageTk.PhotoImage(
    Image.open('./images/python-django.png'))
python_pyspark_img = ImageTk.PhotoImage(
    Image.open('./images/python-pySpark.png'))

image_list = [python_img, python_tkinter_img, python_scikitlearn_img,
              python_flask_img, python_django_img, python_pyspark_img]

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)
status_label = Label(
    root, text=f'Image 1 of {str(len(image_list))}', bd=1, relief=SUNKEN, anchor=E)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status_label = Label(
        root, text=f'Image {str(image_number)} of {str(len(image_list))}', bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status_label = Label(
        root, text=f'Image {str(image_number)} of {str(len(image_list))}', bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(1))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
