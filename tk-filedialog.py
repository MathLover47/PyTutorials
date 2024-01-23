from tkinter import *
from tkinter import filedialog
def open_file():
                file1 = filedialog.askopenfile(mode="r")
                Label(text = file1, bg = "black", fg= "white", font=("times",14,"bold")).pack()
                #file2 = open(file1, mode='rb')
                if file1 != None:
                                data = file1.read()
                                Label(text = data, bg="black", fg="white", font =14).pack()
                
win = Tk()


btn1 = Button(win,text = "Open", command = open_file)
btn1.pack()
win.mainloop()
