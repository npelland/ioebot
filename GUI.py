'''
Simple GUI controller


'''
from tkinter import *

root = Tk()
root.title("IOT Controller")
root.geometry("600x200")
topFrame = Frame(root)
topFrame.pack()
bottomFrame =  Frame(root)
bottomFrame.pack(side=BOTTOM)


button1 = Button(bottomFrame, text="Generate", fg='black')

button1.pack()

variable = StringVar(root)
variable.set("Location") # default value

w = OptionMenu(root, variable, "one", "two", "three")
w.pack(side=LEFT)

variable1 = StringVar(root)
variable1.set("Date") # default value

w = OptionMenu(root, variable1, "one", "two", "three")
w.pack(side=LEFT)

root.mainloop()

