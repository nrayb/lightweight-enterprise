#	GUI File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016
#   Python Version 3.X

    
import Tkinter # GUI Module
import Ctrl # Python file containing GPIO commands

window = Tk()
window.title("BarTini GUI")
window.geometry('800x480') # Screen Resolution

exitButton = Button(window, text="Exit", command=exitPgrm, height=2, width=6)
exitButton.pack(side = BOTTOM)

mainloop()
