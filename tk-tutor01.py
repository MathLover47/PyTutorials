import tkinter
win = tkinter.Tk()
def exit1():
                win.destroy()

win.geometry("200x100")
win.title = "first prgoram of buttons"
b1 = tkinter.Button(win,text = "exit window", bg="white", fg="black", command = exit1)
b1.pack(side ="top")
win.mainloop()
