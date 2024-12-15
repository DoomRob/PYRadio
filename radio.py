from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("My Code")
root.iconbitmap('c:/Users/Documents/Python/GUI')

# Defining the Variable
# rbutton = IntVar()
# rbutton.set("1")

def buttonClick(value):
    label = Label(root, text = value)
    label.pack()

choices = [
    ("Ham", "Cheese"),
    ("Chicken", "Mayo"),
    ("Pork", "Colesaw"),
    ("Tuna", "Tomato"),
]

sandwich = StringVar()
sandwich.set("Cheese")

for text, mode in choices:
    Radiobutton(root, text = text, variable=sandwich, value = mode).pack(anchor=W)

# Creating a radio buttons
# Radiobutton(root, text="Pick 1", variable=rbutton, value=1, command=lambda: buttonClick(rbutton.get())).pack()
# Radiobutton(root, text="Pick 2", variable=rbutton, value=2, command=lambda: buttonClick(rbutton.get())).pack()

# label = Label(root, text = sandwich.get())
# label.pack()

abutton = Button(root, text = "Click", command=lambda: buttonClick(sandwich.get()))
abutton.pack()

root.mainloop()
