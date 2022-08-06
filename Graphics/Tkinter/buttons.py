from tkinter import *

window = Tk()

def toggle(button):
    if button["bg"] == "green":
        button["bg"] = "red"
        button["text"] = "off"
    else:
        button["bg"] = "green"
        button["text"] = "on"

button = Button(
    text="on",
    bg = "green",
    command = lambda: toggle(button)
)
button.pack()

window.mainloop() # starts the graphics, like plt.show()
