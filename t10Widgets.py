from tkinter import *
root= Tk()
root.geometry("655x333")

def getvals():
    print(uservalue.get())
    x=uservalue.get()
    print(passvalue.get())
    y= passvalue.get()
    label = Label(text=x, background="green")
    label.grid()
    print(f"the value of username is {uservalue.get()}")
    print(f"the value of passvalue is {passvalue.get()}")


user = Label(root, text ="Username")
password=  Label(root, text="Password")
# one way of packing is .pack another way is .grid()

user.grid()
password.grid(row=1)

#Variable classes in tkinker
#BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1, column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()