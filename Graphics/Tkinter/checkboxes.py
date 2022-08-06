import tkinter as tk

window = tk.Tk()
window.geometry('100x100')

l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()


def print_selection():
    print(var1.get(), var2.get())

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()
