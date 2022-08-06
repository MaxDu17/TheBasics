from tkinter import *

root = Tk()
root.geometry("200x200")


# Change the label text
def show():
    label.config(text=clicked.get())

# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Monday")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(root, text="click Me", command=show).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()
