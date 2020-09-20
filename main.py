# Import Python Library
import os
from tkinter import *

# Initialize the Tkinter window
userInterface = Tk()

# Title of the tab
userInterface.title("File Manager")

# Set the window size 
userInterface.geometry("275x300")
indentVaule = 60

# Browse for the directory inside the computer
Label(userInterface,text="Directory:").place(x=20,y=20)
linkdir =Entry(userInterface,width =20).place(x=75,y=20)
browsedir = Button(userInterface, background="white" , text ="Browse", command = userInterface.destroy)
browsedir.place(x=205,y=15)

# Do radiobutton to determine what type of sort the client wants
sortVar=IntVar()
Radiobutton(userInterface,text="Sort by File Type",variable = sortVar,value=1).place(x=indentVaule,y=50)
Radiobutton(userInterface,text="Sort by File Size", variable = sortVar,value=2).place(x=indentVaule,y=80)

# Check some of the rules to use during the segregation
condition1 = IntVar()
condition2 = IntVar()
condition3 = IntVar()
condition4 = IntVar()
Checkbutton(userInterface,text="Delete Duplicate Files",variable=condition1).place(x=indentVaule,y=130)
Checkbutton(userInterface,text="Delete Large Files",variable=condition2).place(x=indentVaule, y=150)
Checkbutton(userInterface,text="Delete old files",variable=condition3).place(x=indentVaule,y=170)
Checkbutton(userInterface,text ="Create catalog of sorted files",variable=condition4).place(x=indentVaule,y=190)

# Put execution and cancel button 
executeBtn = Button(userInterface,text="Execute task").place(x=130,y=250)
cancelBtn = Button(userInterface,text="Cancel",command=userInterface.destroy).place(x=210,y=250)

# Loop the user-interface
userInterface.mainloop()

