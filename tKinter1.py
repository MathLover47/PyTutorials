from tkinter import *
gui = Tk()
gui.geometry("400x200+200+100")
gui.title("hello world")

lbl1 = Label(text = "first label", bg="black",fg="lightgreen").place(x=20,y=20)
'''lbl1.pack()'''
lbl2 = Label(text = "second Label", fg = "black", bg = "red")
lbl2.place(x=100,y=40)
lbl3 = Label(text="on Grid", bg="green", fg= "black")
lbl3.grid(row = 3, column = 0,sticky='w')
gui.mainloop()

