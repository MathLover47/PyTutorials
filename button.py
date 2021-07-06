from tkinter import *
win1 = Tk()
win2 = Tk()
win1.title = "Buttons Handling first windows"
win2.title= 'button handling second window'
win1.geometry("400x200+100+100")
win2.geometry("300x400+500+300")
sv = StringVar()
def btn_enter():
                
                lbl = Label(win2,text = sv.get(), bg="green",fg="black",font=10)
                lbl.pack()
def btn_delete():
                lbl2 = Label(win1,text = "you pressed delete", bg="red", fg="white",font=10)
                lbl2.pack()
btnEnter = Button(command = btn_enter,text="Enter",bg="red",fg="brown",font=14)
btnEnter.pack()
btnDelete = Button(win2,text = "delete", fg = "white", bg = "black", font = 15, command = btn_delete)
btnDelete.pack()
txt1 = Entry(textvariable = sv)
txt1.pack()
