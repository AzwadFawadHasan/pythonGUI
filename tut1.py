#print("hellow")
#import tkinter
from tkinter import *

#azwad_root = Tk()
#
##gui logic
#
#azwad_root.mainloop()
##Question = other than Tkinker what are the ways we can create a gui in python?

myRoot = Tk()

# Width x Height
myRoot.geometry("644x234")

#width, height
myRoot.minsize(500,200)

#width, height
myRoot.maxsize(1200,899)

myLabel = Label(text="Pycharm Community edition\n")
myLabel2 = Label(text="Create new Project")
myLabel3= Label(text="Open")
myLabel4= Label(text="Edit a project")
myLabel.pack()#we need to pack after adding label
myLabel2.pack()#we need to pack after adding label
myLabel3.pack()#we need to pack after adding label
myLabel4.pack()#we need to pack after adding label

myRoot.mainloop()
