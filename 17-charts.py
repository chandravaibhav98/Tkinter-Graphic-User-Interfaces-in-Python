from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


root = Tk()
root.title('Charts')
root.iconbitmap('./icons/codemy.ico')
root.geometry("80x80")


def graph():
    house_prices = np.random.normal(20000, 2500, 500)
    plt.hist(house_prices, 100)
    plt.show()


myButton = Button(root, text='Plot', command=graph).pack()


root.mainloop()
