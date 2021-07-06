from tkinter import *
from tkinter import colorchooser
#import tkinter.colorchooser
win = Tk()



def select_color():
                colour = colorchooser.askcolor()
                Label(text = colour[0], bg = colour[1], fg="black").pack()
b1 = Button(text="choose color",bg="white",fg="black",command = select_color).pack()
win.mainloop()
