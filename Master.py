#	GUI File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016

#import Ctrl # Python file containing GPIO commands
import Drinklist # Python file containing recipies
from Tkinter import *
from PIL import ImageTk, Image

# Program for printing variables on button presses. For Testing.
def PrintPrgm(n):
	print(n)
	return
	
# Function to Quit GUI upon pressing the exit button Replace with the one in Ctrl.py when completed.
def exitPrgm():
	print("Exiting Program")
	#GPIO.cleanup()
	window.quit()
	return

# GUI Main Config
window = Tk()
window.title("BarTini GUI")
window.geometry('800x480') # Screen Resolution
window.configure(background='white')

def modalGen(drinkNo):
	modal = Toplevel()
	modal.title("Drink Details")
	modal.geometry('400x240')	
	infostring_var = StringVar()
	infostring = "\nDrink Contains the Following Ingredients:\n"
	for ingredient in Drinklist.drinks[drinkNo]:
		if(ingredient[0] == "Alcohol"):			
			infostring = infostring + "\n" + str(ingredient[2]*45) + "mL of " + ingredient[1]
		else:
			infostring = infostring + "\n" + str(ingredient[2]) + "mL of " + ingredient[1]
	infostring_var.set(infostring + "\n")
	#msg = Label(modal, textvariable=infostring_var, font=("Arial",12)).grid(row=0, column=0, columnspan=6, padx=50, pady=30)
	#make_button = Button(modal, text="Make Drink", command=lambda: PrintPrgm("make_button pressed")).grid(row=1, column=2)
	#cancel_button = Button(modal, text="Cancel", command=modal.destroy).grid(row=2, column=2)
	msg = Label(modal, textvariable=infostring_var, font=("Arial",12)).pack()
	make_button = Button(modal, text="Make Drink", command=lambda: PrintPrgm("make_button pressed")).pack() # This button should invoke the control signal process
	cancel_button = Button(modal, text="Cancel", command=modal.destroy).pack()
	return

# Logo and Company Banner
LE_logo = ImageTk.PhotoImage(Image.open("LE_logo.gif"))
logo_label = Label(window, image=LE_logo)
logo_label.grid(row=0,column=0)
LE_text = Label(window, text="BarTini GUI", font=("Biondi", 30, "bold"), bg='white').grid(row=0,column=1,columnspan=5, sticky=SW)

# Rum and Coke
RC_image = ImageTk.PhotoImage(Image.open("RC.gif"))
RC_button = Button(window, image=RC_image, width="110", height="170", compound=TOP, text="Rum and Coke", command=lambda: modalGen(Drinklist.RC)).grid(row=1, column=0, pady=10, padx=5)

# Screwdriver
SD_image = ImageTk.PhotoImage(Image.open("SD.gif"))
SD_button = Button(window, image=SD_image, width="110", height="170", compound=TOP, text="Screwdriver", command=lambda: modalGen(Drinklist.SD)).grid(row=1, column=1, pady=10, padx=5)

# Whiskey Sour
WS_image = ImageTk.PhotoImage(Image.open("WS.gif"))
WS_button = Button(window, image=WS_image, width="110", height="170", compound=TOP, text="Whiskey Sour", command=lambda: modalGen(Drinklist.WS)).grid(row=1, column=2, pady=10, padx=5)

# Gin Rickey
GR_image = ImageTk.PhotoImage(Image.open("GR.gif"))
GR_button = Button(window, image=GR_image, width="110", height="170", compound=TOP, text="Gin Rickey", command=lambda: modalGen(Drinklist.GR)).grid(row=1, column=3, pady=10, padx=5)

# Daquiri
DAQ_image = ImageTk.PhotoImage(Image.open("DAQ.gif"))
DAQ_button = Button(window, image=DAQ_image, width="110", height="170", compound=TOP, text="Daquiri", command=lambda: modalGen(Drinklist.DAQ)).grid(row=2, column=0, pady=10, padx=5)

# Tom Collins
TC_image = ImageTk.PhotoImage(Image.open("TC.gif"))
TC_button = Button(window, image=TC_image, width="110", height="170", compound=TOP, text="Tom Collins", command=lambda: modalGen(Drinklist.TC)).grid(row=2, column=1, pady=10, padx=5)

# Gimlet
GM_image = ImageTk.PhotoImage(Image.open("RC.gif"))
GM_button = Button(window, image=GM_image, width="110", height="170", compound=TOP, text="Gimlet", command=lambda: modalGen(Drinklist.GM)).grid(row=2, column=2, pady=10, padx=5)

# Long Island Iced Tea
LI_image = ImageTk.PhotoImage(Image.open("LI.gif"))
LI_button = Button(window, image=LI_image, width="110", height="170", compound=TOP, text="Long Island Iced Tea", command=lambda: modalGen(Drinklist.LI)).grid(row=2, column=3, pady=10, padx=5)

# Exit Button
exit_button = Button(window, text="Exit", command=exitPrgm).place(x=740, y=440)

# ***FOR DEBUG*** Print entire drinklist
#def printDrinkList():
	#for drink in Drinklist.drinks:
		#for ingredient in drink:
			#print(ingredient)
			#print("DONE INGREDIENT")
		#print("\nDONE DRINK\n")
	#return
#drinklist_button = Button(window,text="Print All Drinks", command=printDrinkList).grid(row=3,column=0)

mainloop()
