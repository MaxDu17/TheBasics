from tkinter import *
from tkinter import messagebox

win = Tk()

def on_click():
   messagebox.showerror('Python Error', 'Error: This is an Error Message!')

b = Button(win, text="Click Me", command=on_click)
b.pack()

win.mainloop()
