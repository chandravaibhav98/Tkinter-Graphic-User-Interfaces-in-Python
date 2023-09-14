from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="tkinter")
myLabel2 = Label(root, text="chandravaibhav98")


# Display it on screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# ---OR---

myLabel3 = Label(root, text="2-grid").grid(row=1, column=0)
myLabel4 = Label(root, text="Python").grid(row=2, column=1)

root.mainloop()
