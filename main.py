import tkinter as tk
from PIL import Image, ImageTk

def function():
    label.config(text = "Hello, World!")

window = tk.Tk()
imagefile = Image.open("img.jpg")
test = ImageTk.PhotoImage(imagefile)
imagelabel = tk.Label(image=test)
# imagelabel.image = test
imagelabel.place(x=0,y=0)

greeting = tk.Label(text="Hello, Tkinter")
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="#000000",
    width=100,
    height=10
)


def function2(name):
    name = entry.get()
    greeting.config(text = name)

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.bind('<Return>', function2) 

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=function
)
greeting.pack()
label.pack()
entry.pack()
button.pack()

window.mainloop()
