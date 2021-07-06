import tkinter as tk
import time as tm
from tkinter import messagebox as mb
counter = 0
Mwin = tk.Tk()
begin_time = tm.asctime() 
end_time = tm.asctime()
regarded = False
save_begin = True
label1 = tk.Label(font=("roman",47,"bold"), fg="green", bg="black")
label1.pack()
def start_counter():
                global regarded
                regarded = False
                global save_begin
                global begin_time
                if  save_begin == True:
                                begin_time = tm.asctime()
                                save_begin = False
                global counter
                def count():
                                global counter
                                global regarded
                                global label1
                                if  regarded == False:
                                                counter +=1
                                                label1.configure(text = str(counter))
                                                label1.after(1,count)
                count()
def quit_application():
                m = mb.askyesno(title= "quitting without saving",message="are you sure you want to quit")
                if m == 1:
                                Mwin.destroy()
def stop_counter():
                global end_time
                global regarded
                global save_begin
                global counter
                end_time = tm.asctime()
                regarded = True
                save_begin = True
def save_counter():
                file1 = open(".\\savedCounter.txt", "w+")
                str1 = ""
                str1 += "beginng time is:"+begin_time+ "\nEnd time is :"
                str1 += end_time+ "\n Finished in " + str(counter) + "  seconds\n"
                file1.write(str1)
                file1.close()
def reset_counter():
                global counter, label1
                label1.configure(text = "0")
                counter = 0
b1 = tk.Button(text="start |>", fg = "green", bg = "black", command = start_counter,font=("arial",22,"bold"))
b1.pack()
b2 = tk.Button(text = "stop []", fg = "red", bg = "black", command = stop_counter, font = ("times",22,"bold"))
b5 = tk.Button(text = "reset <<=", fg = "red", bg = "black", command = reset_counter, font = ("times",22,"bold"))
b2.pack()
b5.pack()
b3 = tk.Button(text = "Save me", command = save_counter)
b3.pack()
b4 = tk.Button(text = "Quit", command = quit_application)
b4.pack()
Mwin.mainloop()

                                
                
