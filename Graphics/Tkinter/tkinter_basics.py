# this ordering is important
# it's basically saying to override classic tkinter
# with a newer version, if the widgets exist in the newer version
from tkinter import *
# however, there are some compatibility issues. So let's avoid this for now
# from tkinter.ttk import *

window = Tk()


# two things that can be useful
window.title('My Window')
window.attributes('-topmost',True) #keeps the window at the top. Use at your own risk
window.geometry('300x385+1200+500') # point_x x point_y + x_start + y_start

# all paramters are optional
# https://www.tcl.tk/man/tcl/TkCmd/colors.html for all colors
message = Label(text = "Hello world!",
                foreground = "white",
                background = "black",
                width = 20) #width, height determined by dimensions of "0"
# "anchor" is essential how it's alligned. Don't put anything, and it's centered
message.pack(anchor = W) # this puts it into the window. This is a "dummy" way of doing it

button = Button(
    text="Click me!",
    width=25,
    height=5,
    bg="black",
    fg="white" # the text color
)
button.place(x = 0, y = 20) #this is the explicit way of doing it
# button.configure(state = "disabled") # you can disable a button or any other element

another_message = Label(text = "hello again", font=('Calibri 15 bold')) #width, height determined by dimensions of "0"
# pady is distance from the top
another_message.pack(pady = 100) # this puts it into the window. This is a "dummy" way of doing it


window.mainloop() # starts the graphics, like plt.show()
