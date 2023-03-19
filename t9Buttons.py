from tkinter import *
root=Tk()
root.geometry("655x333")

def hello():
    print('its name')
    label = Label(text="hellow was pressed")
    label.pack(side=BOTTOM)

def name():
    print('its name')
    label = Label(text="name was pressed")
    label.pack(side=TOP)

frame = Frame(root,borderwidth=6,bg="grey") 
frame.pack(side=LEFT,anchor="nw")
b1= Button(frame, fg="red", text="print", command=hello)
b2= Button(frame, fg="green", text="print me the name",command=name)
b3= Button(frame, fg="blue", text="print")
b2.pack(side=TOP, padx=5, pady=5)
b3.pack(side=TOP, padx=5, pady=5)
b1.pack(side=TOP, padx=5, pady=5)
root.mainloop()