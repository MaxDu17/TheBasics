import tkinter as tk

window = tk.Tk()

entry = tk.Entry(fg="black", bg="white", width=50)
entry.pack()

def collect_info():
    print(entry.get())
    entry.delete(0, tk.END) #deletes the text (start -> end)
    entry.insert(0, "REPLACEMENT!") #insert something

button = tk.Button(
    text="Submit",
    command = collect_info
)

button.pack()

window.mainloop()
