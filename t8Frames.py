from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("700x560")
root.title("My Window")

f1 = Frame(root, bg="grey", borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

l = Label(f1, text="Enter Image to detect Number plate")
l.pack(pady=260)

f2 = Frame(root, borderwidth=8, background="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f2, text="Detected Number Plate")
l.pack(pady=260)

#root.title("practiseT3")
#rootLabel = Label(text="footer",bg="red")
#rootLabel.pack(side=BOTTOM, fill=X)

root.mainloop()