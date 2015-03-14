import ArraySorter
from Tkinter import *




class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createwidgets(self):

        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
        self.lbl_display.pack({"side": "right"})
        self.lbl_display["Text"] = "Hello"

        #self.txt_display[""] = "Hello there!"

    def __init__(self, master=None):
        self.QUIT = Button(self)
        self.hi_there = Button(self)
        self.lbl_display = Label(self)
        #self.txt_display = Text(self)
        self.pack()
        self.createwidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()