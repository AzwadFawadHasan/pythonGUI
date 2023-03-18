from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("644x234")

#for png
label1 = Label(text="firstImage",background="red")
label1.pack(fill=X)
img1 = PhotoImage(file="1.png")
img1Label = Label(image=img1)
img1Label.pack()


#for jpg
label2= Label(text="SecondJpegImage",background="red")
label2.pack(fill=X)
imgJpeg = Image.open(("index.jpeg"))
img2 = ImageTk.PhotoImage(imgJpeg)
img2Label= Label(image=img2)
img2Label.pack()

root.mainloop()