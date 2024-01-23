from tkinter import *
from tkinter import messagebox
win1 = Tk()

win1.title = "Buttons Handling first windows"
#win2.title= 'button handling second window'
win1.geometry("400x200+100+100")
#win2.geometry("300x400+500+300")
sv = StringVar()
def quitting():
                mes = messagebox.askyesno(title = "Exiting Program", message = "are you sure you want to quit")
                if mes == 1:
                                win1.destroy()
                                
def new_file():
                lbl2 = Label(win1,text = "you pressed new file", bg="black", fg="white",font=("simplified",12,"bold","italic"))
                lbl2.pack()
def save_file():
                lbl3 = Label(win1,text = "you pressed save file", bg="red", fg="white",font=('roman',13,"bold"))
                lbl3.pack()
                messagebox.showinfo(title="Saving file", message= "finished saving") 
def save_as():
                lbl4 = Label(win1,text = "you pressed save as file", bg="black", fg="yellow",font=("verdana",14))
                lbl4.pack()
def btn_enter():
                
                lbl = Label(win1,text = sv.get(), bg="green",fg="black",font=("times",12,"italic"))
                lbl.pack()
def btn_delete():
                lbl2 = Label(win1,text = "you pressed delete", bg="red", fg="white",font=10)
                lbl2.pack()
btnEnter = Button(command = btn_enter,text="Enter",bg="red",fg="brown",font=14)
btnEnter.pack()
btnDelete = Button(win1,text = "delete", fg = "white", bg = "black", font = 15, command = btn_delete)
btnDelete.pack()
txt1 = Entry(textvariable = sv)
txt1.pack()
Mymenu = Menu(win1)
MenuOne = Menu()
MenuSub = Menu()
MenuSub.add_command(label="*.text", command = save_as)
MenuSub.add_command(label= "*.*", command = save_as)
MenuOne.add_command(label="New", command = new_file)
MenuOne.add_command(label="Save", command = save_file)
MenuOne.add_cascade(label = "Save as", menu = MenuSub)
Mymenu.add_cascade(label="File", menu=MenuOne)
Mymenu.add_cascade(label="Edit")
Mymenu.add_cascade(label="Format")
Mymenu.add_cascade(label='Run')
Mymenu.add_command(label = "quit", command = quitting)

win1.configure(menu = Mymenu)
