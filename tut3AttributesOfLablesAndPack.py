from tkinter import *

import xdg
root = Tk()
root.geometry("444x233")

root.title("myAppilication")

#important lablel options
#texts=>adds the text
#bd = background
#fg = foregrround
#font = sets font
# padx = x padding
# pady = y padding
#relief - border styling - sunken raised groove rdige

title_label = Label(text='''my text\n
A high-quality paragraph generator t\nransforms everyone on your team into a robust and well-rounded writer. Now anyone can create informative, engaging, and persuasive \ncontent one paragraph at a time – whether responding to a lead via email or creating a thought leadership piece \n, to go viral.''', bg="red", foreground="white", padx=23, pady=94, font=("comicsansms",19), borderwidth=3, relief=SUNKEN)
title_label.pack(side=BOTTOM,anchor="nw", fill=X)
#fill fills up either from x as the screen is extended
#side = top bottom left right
#anchor = "nw"/"se" etc



root.mainloop()