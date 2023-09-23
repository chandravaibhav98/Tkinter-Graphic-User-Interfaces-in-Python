from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Message boxes')
root.iconbitmap('./icons/codemy.ico')

# messagebox.showinfo("Message box", 'Info')
# messagebox.showwarning("Message box", 'Warning')
# messagebox.showerror("Message box", 'Error')
# messagebox.askquestion("Message box", 'Question')
# messagebox.askokcancel("Message box", 'Ok/Cancel')
# messagebox.askyesno("Message box", 'Yes/No')


def popup():
    response = messagebox.askyesno("Message box", 'Yes/No')
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text=f'You made a Positive Response : {response}').pack()
    else:
        Label(root, text=f'You made a Negative Response : {response}').pack()


Button(root, text='Popup', command=popup).pack()

root.mainloop()
