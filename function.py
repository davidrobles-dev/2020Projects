# PROJECT NAME: Log-in/out and Sign-up user interface
# DEVELOPER: @davidrobles-dev
# START DATE: 01 Nov 2020 154400
# END DATE:
# PROJECT DESCRIPTION: Create the log-in, log-out and Sign-up sequence 

# ********************************************************************
#                       Importing needed library
# ********************************************************************
from tkinter import *
import os

# Initialize window name
log = Tk()
log.title("Masiter Flower Shop") # Name of the app window
log.geometry("1000x600") # Userinterface W x L 

# Setup the window widgets
def placeLabel(Ui,Greetings):
    Label(Ui,text= Greetings + "\n").pack()

# Check for the file or create the file that served as database
logfile = open("Users.txt","w+")

placeLabel(log,"Welcome to Trident PoS System!")
placeLabel(log,"123")

# Loop the user-interface
log.mainloop()

