__author__ = 'mohamed'
from Tkinter import *

root = Tk()
thelabel = Label(root, text="hello")
thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text="button1", fg="red")
button2 = Button(topFrame, text="button2", fg="green")
button3 = Button(bottomFrame, text="button3", fg="blue")
button4 = Button(bottomFrame, text="button4", fg="yellow")

# prints my name


def printname(event):
    print "Hello my name is Mohamed"


button1.bind("<Button-1>", printname)
button1.pack(side=RIGHT)
button2.pack()
button3.pack(side=RIGHT)
button4.pack()

root.mainloop()