import tkinter as tk

window = tk.Tk()
window.attributes('-topmost',True) #keeps the window at the top. Use at your own risk

def close_routine(second_window):
    print("closed!")
    second_window.destroy()

def collect_info():
    second_window = tk.Toplevel() #same type as "window" but another one
    message = tk.Label(second_window, text="Hello world!") #add "second_window" to tell it where to put the text
    message.pack()
    second_window.after(1, lambda: second_window.focus_force())
    # just in case you want to have a window close event. Totally optional
    second_window.protocol("WM_DELETE_WINDOW", lambda: close_routine(second_window))

button = tk.Button(
    text="Pop!",
    command = collect_info
)

button.pack()

window.mainloop()
