from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
def show_combo(e):
                messagebox.showinfo( title = "Selection", message=cb1.get())
def show_on_label():
                global label1
                label1.configure(text = sb.get())
win1 = Tk()
cb1 = Combobox(win1, width = 40, height= 20,values= (1,2,3,4,5,6))

cb1['values']=(98,888,333,"hello")
cb1.current(3)
cb1.bind("<<ComboboxSelected>> ",show_combo)
cb1.pack(side = 'left')
label1 = Label(win1,text = "spin your value",font =("arial", 24,"bold"))
label1.pack()
sb = Spinbox(from_ = 0, to = 100, increment = 5, command = show_on_label)
sb.pack(side = 'right')
win1.mainloop()

