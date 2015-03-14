__author__ = 'mosamy'
from Tkinter import *

root = Tk()
theLabel = Label(root, text="Hello")
theLabel.pack()
root.title = "My first Tkinter window"
root.maxsize()
root.mainloop()
