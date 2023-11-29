import tkinter

# from tkinter import * --> then we can get rid of tkinter. when we are calling a method in this class

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# label
# my_label = tkinter.Label(text="I am a LABEL", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label = tkinter.Label(text="I am a LABEL")
my_label.pack()

# Changing the text message, 2 ways:
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text=input_box.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input_box = tkinter.Entry(width=10)
input_box.pack()

window.mainloop()
