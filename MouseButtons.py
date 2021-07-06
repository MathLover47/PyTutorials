from tkinter import *
win = Tk()
win.geometry("800x400+200+100")
def click_middle1(e):
                l1=Label(win, fg="black", bg="green",text = "Mid button clicked").pack()
def click_left1(e):
                l2=Label(win,text = "Left button clicked" , fg="red", bg="black").pack()
def click_right1(e):
                l3=Label(win, fg="white", bg="blue",text = "Right button clicked").pack()
win.bind("<Button-1>", click_left1)
win.bind("<Button-2>", click_middle1)
win.bind("<Button-3>", click_right1)
win.mainloop()
