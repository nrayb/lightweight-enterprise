#	GUI File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016

#import Ctrl # Python file containing GPIO commands
import Drinklist # Python file containing recipies
from Tkinter import *
from PIL import ImageTk, Image
	
# Function to Quit GUI upon pressing the exit button. Might need to add raspberry pi cleanup. Should be placed in Ctrl.py when done.
def exitPrgm():
	print("Exiting Program")
	#GPIO.cleanup()
	window.quit()
	return

# GUI Main Config
window = Tk()
window.title("BarTini GUI")
window.geometry('800x480+0+0') # Screen Resolution
window.configure(background='white')
#window.attributes("-fullscreen", True)

# Load Drink Quantites from txt file on startup
Drinklist.LoadQuantities()

# Local Custom Ingredient Strings
i0 = ["None","None",0]
i1 = ["None","None",0]
i2 = ["None","None",0]
i3 = ["None","None",0]
i4 = ["None","None",0]

# Wrapper Function to modify the custom drink recipe
# Called by pressing save button in cmodal
MAXQUANTITY = 500
def save_custom(l0,q0,l1,q1,l2,q2,l3,q3,l4,q4):
	
	# Handle case of empty string for quantity
	if(q0 == ""):
		q0 = "0"
	if(q1 == ""):
		q1 = "0"
	if(q2 == ""):
		q2 = "0"
	if(q3 == ""):
		q3 = "0"
	if(q4 == ""):
		q4 = "0"
	
	if((int(q0)+int(q1)+int(q2)+int(q3)+int(q4))>MAXQUANTITY):
		# Quantity totals too much. Drink not saved. Display message to user
		quantityerror = Toplevel()
		quantityerror.title("Quantity Error")
		quantityerror.geometry('300x180')
		qe_txt = "Total drink quantity is too high.\nCannot exceed " + str(MAXQUANTITY) + "mL in total liquids.\nPlease re-edit your recipe."
		msg = Label(quantityerror, text=qe_txt, font=("Arial",12)).pack()
		OK_button = Button(quantityerror, text="OK", command=quantityerror.destroy).pack()
		return
	
	# Save local variables
	#if (l0 != "None"):
	save_i0(l0,q0)
	#if (l1 != "None"):
	save_i1(l1,q1)
	#if (l2 != "None"):
	save_i2(l2,q2)
	#if (l3 != "None"):
	save_i3(l3,q3)
	#if (l4 != "None"):
	save_i4(l4,q4)
		
	# Save local variables to Recipe
	Drinklist.CustomizeDrink(i0,i1,i2,i3,i4)
	return

# Internal Functions to set temporary local variables
# Used in modifying the custom drink recipe.
# Called by save_custom defined above	
def save_i0(liquid,quantity):
	i0[1] = liquid
	i0[2] = int(quantity)
	for alc in Drinklist.ALCOHOLS:
		if liquid == alc:
			i0[0] = "Alcohol"
			return
	if (liquid != "None"):
		i0[0] = "Mixer"
	else:
		i0[0] = "None"
	return
	
def save_i1(liquid,quantity):
	i1[1] = liquid
	i1[2] = int(quantity)
	for alc in Drinklist.ALCOHOLS:
		if liquid == alc:
			i1[0] = "Alcohol"
			return
	if (liquid != "None"):
		i1[0] = "Mixer"
	else:
		i1[0] = "None"
	return

def save_i2(liquid,quantity):
	i2[1] = liquid
	i2[2] = int(quantity)
	for alc in Drinklist.ALCOHOLS:
		if liquid == alc:
			i2[0] = "Alcohol"
			return
	if (liquid != "None"):
		i2[0] = "Mixer"
	else:
		i2[0] = "None"
	return
	
def save_i3(liquid,quantity):
	i3[1] = liquid
	i3[2] = int(quantity)
	for alc in Drinklist.ALCOHOLS:
		if liquid == alc:
			i3[0] = "Alcohol"
			return
	if (liquid != "None"):
		i3[0] = "Mixer"
	else:
		i3[0] = "None"
	return

def save_i4(liquid,quantity):
	i4[1] = liquid
	i4[2] = int(quantity)
	for alc in Drinklist.ALCOHOLS:
		if liquid == alc:
			i4[0] = "Alcohol"
			return
	if (liquid != "None"):
		i4[0] = "Mixer"
	else:
		i4[0] = "None"
	return
	
def QuantityVerifyStep(drinkNo, modal):
	
	print("Verifing Quantities...\n")
	
	# Check for insufficient amounts
	for ingredient in Drinklist.drinks[drinkNo]:
		for drink in Drinklist.QuantityTracking:
			# Find liquid in quantity variable
			if drink[0] == ingredient[1]:
				if drink[1] < ingredient[2]:
					# Not sufficient amound remaining
					print("Invalid Quantities Detected...")
					errmsg = Toplevel()
					errmsg.title("Quantity Error")
					errmsg.geometry('400x200+300+150')
					textmsg = StringVar(errmsg)
					textmsg.set("Insufficient amount of " + ingredient[1])
					content = Label(errmsg, textvariable=textmsg).pack()
					ok_button = Button(errmsg, text="OK", command=errmsg.destroy).pack()
					return
	
	print("Valid Quantities Detected...")				
	# Subtract Amounts
	for ingredient in Drinklist.drinks[drinkNo]:
		for drink in Drinklist.QuantityTracking:
			# Find liquid in quantity variable
			if drink[0] == ingredient[1]:
				# Subtract amount from variable
				print("Subtracting " + str(ingredient[2]) + " from " + str(drink[1]) + " in " + ingredient[1])
				drink[1] -= ingredient[2]
	# Write updated variable to text file
	Drinklist.SaveQuantities(Drinklist.QuantityTracking)
	
	# Begin Control Sequence
	print("Initializing Control Sequence")
	#Ctrl.MakeDrink(drinkNo)
	modal.destroy()
	return
			
# Standard Modal
# Called by predefined drink button press
def modalGen(drinkNo):
	modal = Toplevel()
	modal.title("Drink Details")
	modal.geometry('400x240+250+120')
	#modal.attributes("-fullscreen", True)	
	infostring_var = StringVar(modal)
	infostring = "\nDrink Contains the Following Ingredients:\n"
	for ingredient in Drinklist.drinks[drinkNo]:
		if(ingredient[0] == "Alcohol"):			
			infostring = infostring + "\n" + str(ingredient[2]) + "mL of " + ingredient[1]
		elif (ingredient[0] == "Mixer"):
			infostring = infostring + "\n" + str(ingredient[2]) + "mL of " + ingredient[1]
	infostring_var.set(infostring + "\n")	
	msg = Label(modal, textvariable=infostring_var, font=("Arial",12)).pack()
	make_button = Button(modal, text="Make Drink", bg="green", fg="white", command=lambda: QuantityVerifyStep(drinkNo, modal)).pack() # This button should invoke the control signal process
	cancel_button = Button(modal, text="Cancel", command=modal.destroy).pack()
	return
	
# Ingredient Quantity Input Validation
# Function limits input to 3 numeric characters
MAXCHARS = 3
def quantitylimit(P):
	if (len(P) > MAXCHARS):
		return False
	elif P=="":
		return True
	else:		
		try:
			int(P)
			return True
		except ValueError:
			return False

# Customization Modal
# Called by custom drink button press
# Supports up to 5 ingredients
def CustomModal():	
	
	# Basic Config
	cmodal = Toplevel()
	cmodal.title("Custom Drink")
	cmodal.geometry('500x340+200+70')	
	#cmodal.attributes("-fullscreen", True)
	
	# Dropdown Liquid (lx) Variables.
	l0 = StringVar(cmodal)
	l0.set(Drinklist.drinks[Drinklist.CUSTOM][0][1])
	l1 = StringVar(cmodal)
	l1.set(Drinklist.drinks[Drinklist.CUSTOM][1][1])
	l2 = StringVar(cmodal)
	l2.set(Drinklist.drinks[Drinklist.CUSTOM][2][1])
	l3 = StringVar(cmodal)
	l3.set(Drinklist.drinks[Drinklist.CUSTOM][3][1])
	l4 = StringVar(cmodal)
	l4.set(Drinklist.drinks[Drinklist.CUSTOM][4][1])
	
	# Quantities Text Boxes
	q0 = StringVar(cmodal)
	q0.set(str(Drinklist.drinks[Drinklist.CUSTOM][0][2]))
	q1 = StringVar(cmodal)
	q1.set(str(Drinklist.drinks[Drinklist.CUSTOM][1][2]))
	q2 = StringVar(cmodal)
	q2.set(str(Drinklist.drinks[Drinklist.CUSTOM][2][2]))
	q3 = StringVar(cmodal)
	q3.set(str(Drinklist.drinks[Drinklist.CUSTOM][3][2]))
	q4 = StringVar(cmodal)
	q4.set(str(Drinklist.drinks[Drinklist.CUSTOM][4][2]))	
	
	# Labels for Dropdown Boxes and Fillable Text Form
	msg0 = Label(cmodal, text="Ingredient").grid(row=0,column=0,padx=15,pady=10)
	msg1 = Label(cmodal, text="Quantity (in mL)").grid(row=0,column=1,padx=15,pady=10)	
	
	# Validation command wrapper. Invokes quantitylimit in 'key' press.
	vcmd = (cmodal.register(quantitylimit),'%P')
	
	# First Ingredient
	o00 = OptionMenu(cmodal, l0, *Drinklist.MASTER_OPTIONS).grid(row=1,column=0,padx=15)
	o01 = Entry(cmodal, textvariable=q0, width="3", validate='key', validatecommand=vcmd).grid(row=1,column=1,padx=15)	
	
	# Second Ingredient
	o10 = OptionMenu(cmodal, l1, *Drinklist.MASTER_OPTIONS).grid(row=2,column=0,padx=15)
	o11 = Entry(cmodal, textvariable=q1, width="3", validate='key', validatecommand=vcmd).grid(row=2,column=1,padx=15)
	
	# Third Ingredient
	o20 = OptionMenu(cmodal, l2, *Drinklist.MASTER_OPTIONS).grid(row=3,column=0,padx=15)
	o21 = Entry(cmodal, textvariable=q2, width="3", validate='key', validatecommand=vcmd).grid(row=3,column=1,padx=15)
	
	# Fourth Ingredient
	o30 = OptionMenu(cmodal, l3, *Drinklist.MASTER_OPTIONS).grid(row=4,column=0,padx=15)
	o31 = Entry(cmodal, textvariable=q3, width="3", validate='key', validatecommand=vcmd).grid(row=4,column=1,padx=15)
	
	# Fifth Ingredient
	o40 = OptionMenu(cmodal, l4, *Drinklist.MASTER_OPTIONS).grid(row=5,column=0,padx=15)
	o41 = Entry(cmodal, textvariable=q4, width="3", validate='key', validatecommand=vcmd).grid(row=5,column=1,padx=15)
	
	CUSTOM_image_label = Label(cmodal, image=CUSTOM_image).grid(row=1, column=2, padx=15, rowspan=5)
	
	save_drink = Button(cmodal, text="Save Recipie", width="20", bg="blue", fg="white", command=lambda: save_custom(l0.get(), q0.get(), l1.get(), q1.get(), l2.get(), q2.get(), l3.get(), q3.get(), l4.get(), q4.get())).grid(row=6, column=1, pady=5)
	CONT_B_COLOR = "#a51aae" # Hex code corresponding to the purple color of the continue button
	continue_button = Button(cmodal, text="Continue >>", bg=CONT_B_COLOR, fg="white", command=lambda: CustomContWrapper(cmodal)).grid(row=7, column=1)
	cancel_button = Button(cmodal, text="Cancel", command=cmodal.destroy).grid(row=7,column=2, padx=15, pady=5)
	return
	
def CustomContWrapper(cmodal):
	cmodal.destroy()
	modalGen(Drinklist.CUSTOM)
	return

# Logo and Company Banner
LE_logo = ImageTk.PhotoImage(Image.open("LE_logo.gif"))
logo_label = Label(window, image=LE_logo)
logo_label.grid(row=0,column=0)
LE_text = Label(window, text="BarTini GUI", font=("Biondi", 30, "bold"), bg='white').grid(row=0,column=1,columnspan=5, sticky=SW)

# Cuba Libre
CL_image = ImageTk.PhotoImage(Image.open("CL.gif"))
CL_button = Button(window, image=CL_image, width="110", height="170", compound=TOP, text="Cuba Libre", command=lambda: modalGen(Drinklist.CL)).grid(row=1, column=0, pady=10, padx=5)

# Whiskey Cola
WC_image = ImageTk.PhotoImage(Image.open("WC.gif"))
WC_button = Button(window, image=WC_image, width="110", height="170", compound=TOP, text="Whiskey Cola", command=lambda: modalGen(Drinklist.WC)).grid(row=1, column=1, pady=10, padx=5)

# Cubata
CBA_image = ImageTk.PhotoImage(Image.open("CBA.gif"))
CBA_button = Button(window, image=CBA_image, width="110", height="170", compound=TOP, text="Cubata", command=lambda: modalGen(Drinklist.CBA)).grid(row=1, column=2, pady=10, padx=5)

# Gin Rickey
GR_image = ImageTk.PhotoImage(Image.open("GR.gif"))
GR_button = Button(window, image=GR_image, width="110", height="170", compound=TOP, text="Gin Rickey", command=lambda: modalGen(Drinklist.GR)).grid(row=1, column=3, pady=10, padx=5)

# Whiskey Lime
WL_image = ImageTk.PhotoImage(Image.open("WL.gif"))
WL_button = Button(window, image=WL_image, width="110", height="170", compound=TOP, text="Whiskey Lime", command=lambda: modalGen(Drinklist.WL)).grid(row=2, column=0, pady=10, padx=5)

# Screwdriver
SD_image = ImageTk.PhotoImage(Image.open("SD.gif"))
SD_button = Button(window, image=SD_image, width="110", height="170", compound=TOP, text="Screwdriver", command=lambda: modalGen(Drinklist.SD)).grid(row=2, column=1, pady=10, padx=5)

# Gimlet
GM_image = ImageTk.PhotoImage(Image.open("GM.gif"))
GM_button = Button(window, image=GM_image, width="110", height="170", compound=TOP, text="Gimlet", command=lambda: modalGen(Drinklist.GM)).grid(row=2, column=2, pady=10, padx=5)

# Jamaica Glow
JG_image = ImageTk.PhotoImage(Image.open("JG.gif"))
JG_button = Button(window, image=JG_image, width="110", height="170", compound=TOP, text="Jamaica Glow", command=lambda: modalGen(Drinklist.JG)).grid(row=2, column=3, pady=10, padx=5)

# Custom
CUSTOM_image = ImageTk.PhotoImage(Image.open("CUSTOM.gif"))
CUSTOM_button = Button(window, image=CUSTOM_image, width="110", height="170", compound=TOP, text="Custom", command=CustomModal).grid(row=2, column=4, pady=10, padx=5)

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

# ***FOR DEBUG*** Print Specific Drink Recipe
def printRecipe(drinkNo):
	for ingredient in Drinklist.drinks[drinkNo]:
		print(ingredient)
	print("\n")
	return

mainloop()
