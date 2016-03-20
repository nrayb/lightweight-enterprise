#	Drinklist File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016

# Top Array. 3 levels of list. Each drink has a list of ingredients. Each ingredient has a list of labels.
drinks = []

# Contents of Machine
ALCOHOLS = ["Vodka","Rum","Gin","Whiskey"]
MASTER_OPTIONS = ["None","Vodka","Rum","Gin","Whiskey","Cola", "Lime Juice", "OJ", "Lemon Juice", "Soda Water", "Simple Syrup"]

# Quantities located in "quantities.txt" and persist over instances of the program
QuantityTracking = [ ["Vodka", 0], ["Rum", 0], ["Gin", 0], ["Whiskey", 0], ["Cola", 0], ["Lime Juice", 0], ["OJ", 0], ["Lemon Juice", 0], ["Soda Water", 0], ["Simple Syrup", 0] ]

# DrinkNo Correspondances
RC = 0 # Rum and Coke
SD = RC+1 # Screwdriver
WS = SD+1 # Whiskey Sour
GR = WS+1 # Gin Rickey
DAQ = GR+1 # Daiquiri
TC = DAQ+1 # Tom Collins
GM = TC+1 # Gimlet
LI = GM+1 # Long Island Ice Tea
CUSTOM = LI+1 # Custom Drink

mL_PER_SHOT = 45 # Constant Integer

# Drink/Recipe List
# Format for Alcohol: ("Alcohol", "<Type>", <# shots>*45)
# Format for Mixer: ("Mixer", "<Type>", mL)

drinks.insert(RC,[])
drinks[RC].insert(0, ["Alcohol", "Rum", 1*mL_PER_SHOT])
drinks[RC].insert(1, ["Mixer", "Cola", 250])
drinks[RC].insert(2, ["Mixer", "Lime Juice", 45])

drinks.insert(SD,[])
drinks[SD].insert(0, ["Alcohol", "Vodka", int(1.5*mL_PER_SHOT)])
drinks[SD].insert(1, ["Mixer", "OJ", 250])

drinks.insert(WS,[])
drinks[WS].insert(0, ["Alcohol", "Whiskey", 2*mL_PER_SHOT])
drinks[WS].insert(1, ["Mixer", "Lemon Juice", 45])
drinks[WS].insert(2, ["Mixer", "Simple Syrup", 20])

drinks.insert(GR,[])
drinks[GR].insert(0, ["Alcohol", "Gin", 2*mL_PER_SHOT])
drinks[GR].insert(1, ["Mixer", "Soda Water", 200])
drinks[GR].insert(2, ["Mixer", "Lime Juice", 30])

drinks.insert(DAQ,[])
drinks[DAQ].insert(0, ["Alcohol", "Rum", 2*mL_PER_SHOT])
drinks[DAQ].insert(1, ["Mixer", "Simple Syrup", 45])
drinks[DAQ].insert(2, ["Mixer", "Lime Juice", 45])

drinks.insert(TC,[])
drinks[TC].insert(0, ["Alcohol", "Gin", 2*mL_PER_SHOT])
drinks[TC].insert(1, ["Mixer", "Simple Syrup", 30])
drinks[TC].insert(2, ["Mixer", "Lemon Juice", 30])
drinks[TC].insert(3, ["Mixer", "Soda Water", 200])

drinks.insert(GM,[])
drinks[GM].insert(0, ["Alcohol", "Gin", 2*mL_PER_SHOT])
drinks[GM].insert(1, ["Mixer", "Simple Syrup", 20])
drinks[GM].insert(2, ["Mixer", "Lime Juice", 45])

drinks.insert(LI,[])
drinks[LI].insert(0, ["Alcohol", "Gin", 1*mL_PER_SHOT])
drinks[LI].insert(1, ["Alcohol", "Vodka", 1*mL_PER_SHOT])
drinks[LI].insert(2, ["Alcohol", "Rum", 1*mL_PER_SHOT])
drinks[LI].insert(3, ["Mixer", "Lime Juice", 45])
drinks[LI].insert(4, ["Mixer", "Cola", 135])

# Default Custom Drink
drinks.insert(CUSTOM,[])
drinks[CUSTOM].insert(0, ["None", "None", 0])
drinks[CUSTOM].insert(1, ["None", "None", 0])
drinks[CUSTOM].insert(2, ["None", "None", 0])
drinks[CUSTOM].insert(3, ["None", "None", 0])
drinks[CUSTOM].insert(4, ["None", "None", 0])

# Custom Drink Logic
# Currently Allows for ["None", "None", 0] to be a valid entry in the recipe
def CustomizeDrink(ingr0,ingr1,ingr2,ingr3,ingr4):
	drinks[CUSTOM] = [];
	custom_ingr_no = 0
	#if (ingr0[1] != "None"):		
	drinks[CUSTOM].insert(custom_ingr_no, ingr0)
	custom_ingr_no += 1
	#if (ingr1[1] != "None"):
	drinks[CUSTOM].insert(custom_ingr_no, ingr1)
	custom_ingr_no += 1
	#if (ingr2[1] != "None"):
	drinks[CUSTOM].insert(custom_ingr_no, ingr2)
	custom_ingr_no += 1
	#if (ingr3[1] != "None"):
	drinks[CUSTOM].insert(custom_ingr_no, ingr3)
	custom_ingr_no += 1
	#if (ingr4[1] != "None"):
	drinks[CUSTOM].insert(custom_ingr_no, ingr4)	
	return;
	
def LoadQuantities():
	f = open('quantities.txt', 'r')
	for index,line in enumerate(f):
		QuantityTracking[index][1] = int(line)
	print("Imported QuantityTracking.")
	f.close()
	return
	
def SaveQuantities(QuantityTracking):
	f = open('quantities.txt', 'w')
	print("\nWriting to quantity.txt")
	for data_pair in QuantityTracking:
		f.write(str(data_pair[1]) + "\n")
		print("Writing " + str(data_pair[1]))
	print("Done Editing.\n")
	f.close()
	return
