# Import Python Library
import os
from tkinter import *

# Initialize the Tkinter window
userInterface = Tk()

# Title of the tab
userInterface.title("File Management System")

# Set the window size 
userInterface.geometry("320x150")

# Browse for the directory inside the computer
Label(userInterface,text="Directory:",padx=10,pady=10).grid(row=1,column=0)
linkdir =Entry(userInterface,width =30).grid(row=1,column=1)
browsedir = Button(userInterface, background="white" , text ="Browse", command = userInterface.destroy)
browsedir.grid(row=1,column=2)

# Check some of the rules to use during the segregation
condition1 = IntVar()
condition2 = IntVar()
condition3 = IntVar()
Checkbutton(userInterface,text="Delete Duplicate Files",variable=condition1).grid()
Checkbutton(userInterface,text="Delete Large Files",variable=condition2).grid()
Checkbutton(userInterface,text="Generate Catalog for all files sorted",variable=condition3).grid()

# Loop the user-interface
userInterface.mainloop()


