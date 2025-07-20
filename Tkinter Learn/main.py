from tkinter import *

root = Tk()

# Create Widgets
#myLabel1 = Label(root, text="Hello Shreyas mate dude wtf is up mang")
#myLabel2 = Label(root, text="Hello Shreyas mate dude wtf is up mang")

# Put Widgets on screen
#myLabel1.grid(row = 0, column= 0)
#myLabel2.grid(row = 1, column= 1)


e = Entry(root, width=80)
e.pack()
e.insert(0, "Type something")
e.get()

# Functions for Buttons

def addEntry():

    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()
        
        
# Create Buttons

AddEntryButton = Button(root, text="Click Me", command=addEntry)

# Draw Buttons

AddEntryButton.pack()

root.mainloop()