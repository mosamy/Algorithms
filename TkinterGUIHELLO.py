__author__ = 'mohamed'
from Tkinter import *
#import ArraySorter

root = Tk()


thetextbox = Entry(root)
thetextbox.pack()
thelabel = Label(root, text="hello")
thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text="button1", fg="red")
button2 = Button(topFrame, text="log(n)", fg="green")
button3 = Button(bottomFrame, text="button3", fg="blue")
button4 = Button(bottomFrame, text="button4", fg="yellow")


def logn(event):
    n = int(thetextbox.get())

    result = 0
    while n > 1:
        n //= 2
        result += 1
    thetextbox.delete(0, END)
    thetextbox.insert(0, result)

def printname(event):
    #print "Hello my name is Mohamed"
    thetextbox.insert(0, "Hello my name is Mohamed")
    #thetextbox.get()

button1.bind("<Button-1>", printname)
button1.pack(side=RIGHT)
button2.bind("<Button-1>",logn)
button2.pack()
button3.pack(side=RIGHT)
button4.pack()

root.mainloop()