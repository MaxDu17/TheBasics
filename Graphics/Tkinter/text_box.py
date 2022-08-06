import tkinter as tk

window = tk.Tk()

textbox = tk.Text(height = 8, width = 31) #opens up a text box
textbox.pack()

def add_line():
    #insert at row 0 (beginning) column 0
    textbox.insert("0.0", "get vectored!\n")

def remove_line():
    textbox.delete("0.0", "2.0") #remove the first row

def read_everything():
    print(textbox.get("0.0", tk.END)) #read the whole thing and print it out

button = tk.Button(
    text="Add",
    command = add_line
)
button.pack()

button = tk.Button(
    text="Remove",
    command = remove_line
)
button.pack()

button = tk.Button(
    text="Read",
    command = read_everything
)
button.pack()

window.mainloop()
