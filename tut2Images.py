from tkinter import *
from PIL import Image, ImageTk
# first import  sudo apt-get install python3-pil.imagetk
myRoot = Tk()

myRoot.geometry("455x644")

#to add photo into gui use photoImage class
#photo  = PhotoImage(file="1.png")


#for jpeg images
photoJpg  = Image.open("index.jpeg")
photo2 = ImageTk.PhotoImage(photoJpg)
myLabel = Label(image=photo2)
myLabel.pack()

myRoot.mainloop()