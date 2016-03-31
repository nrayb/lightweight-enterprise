#	Drinklist File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016

# Top Array. 3 levels of list. Each drink has a list of ingredients. Each ingredient has a list of labels.
drinks = []

# Contents of Machine
ALCOHOLS = ["Vodka","Rum","Gin","Whiskey"]
MASTER_OPTIONS = ["None","Vodka","Rum","Gin","Whiskey","Cola", "Lime Juice", "Orange Juice", "Soda Water", "Water"]

# Quantities located in "quantities.txt" and persist over instances of the program
QuantityTracking = [ ["Vodka", 0], ["Rum", 0], ["Gin", 0], ["Whiskey", 0], ["Cola", 0], ["Lime Juice", 0], ["Orange Juice", 0], ["Soda Water", 0] ]

# DrinkNo Correspondances
CL = 0 # Cuba Libre
WC = CL+1 # Whiskey Cola
CBA = WC+1 # Cubata
GR = CBA+1 # Gin Rickey
WL = GR+1 # Whiskey Lime
SD = WL+1 # Screwdriver
JG = SD+1 # Jamaica Glow
GM = JG+1 # Gimlet
CUSTOM = GM+1 # Custom Drink

mL_PER_SHOT = 45 # Constant Integer

# Drink/Recipe List
# Format for Alcohol: ("Alcohol", "<Type>", <# shots>*45)
# Format for Mixer: ("Mixer", "<Type>", mL)

drinks.insert(CL,[])
drinks[CL].insert(0, ["Alcohol", "Rum", 1*mL_PER_SHOT])
drinks[CL].insert(1, ["Mixer", "Cola", 150])
drinks[CL].insert(2, ["Mixer", "Lime Juice", 45])

drinks.insert(WC,[])
drinks[WC].insert(0, ["Alcohol", "Whiskey", 1*mL_PER_SHOT])
drinks[WC].insert(1, ["Mixer", "Cola", 150])

drinks.insert(CBA,[])
drinks[CBA].insert(0, ["Alcohol", "Gin", 2*mL_PER_SHOT])
drinks[CBA].insert(1, ["Mixer", "Lime Juice", 35])
drinks[CBA].insert(2, ["Mixer", "Cola", 90])

drinks.insert(GR,[])
drinks[GR].insert(0, ["Alcohol", "Gin", 2*mL_PER_SHOT])
drinks[GR].insert(1, ["Mixer", "Soda Water", 200])
drinks[GR].insert(2, ["Mixer", "Lime Juice", 30])

drinks.insert(WL,[])
drinks[WL].insert(0, ["Alcohol", "Whiskey", int(1.5*mL_PER_SHOT)])
drinks[WL].insert(1, ["Mixer", "Lime Juice", 30])

drinks.insert(SD,[])
drinks[SD].insert(0, ["Alcohol", "Vodka", 1*mL_PER_SHOT])
drinks[SD].insert(1, ["Mixer", "Orange Juice", 135])

drinks.insert(JG,[])
drinks[JG].insert(0, ["Alcohol", "Gin", 2*mL_PER_SHOT])
drinks[JG].insert(1, ["Alcohol", "Rum", int(0.5*mL_PER_SHOT)])
drinks[JG].insert(2, ["Mixer", "Orange Juice", 30])

drinks.insert(GM,[])
drinks[GM].insert(0, ["Alcohol", "Gin", 1*mL_PER_SHOT])
drinks[GM].insert(1, ["Mixer", "Lime Juice", 20])


# Default Custom Drink
drinks.insert(CUSTOM,[])
drinks[CUSTOM].insert(0, ["None", "None", 0])
drinks[CUSTOM].insert(1, ["None", "None", 0])
drinks[CUSTOM].insert(2, ["None", "None", 0])
drinks[CUSTOM].insert(3, ["None", "None", 0])
drinks[CUSTOM].insert(4, ["None", "None", 0])

# Custom Drink Logic
# Currently Allows for ["None", "None", 0] to be a valid entry in the recipe
# Inputs are the ingredients in the same format as the predefined ingredients. This parsing done in Master.py.
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

# Function loads the drink quantities from the text file. Invoked on application launch.	
def LoadQuantities():
	f = open('quantities.txt', 'r')
	for index,line in enumerate(f):
		QuantityTracking[index][1] = int(line)
	print("Imported QuantityTracking.")
	f.close()
	return

# Function to update text file containing drink quantities. Called after a drink is dispensed.	
def SaveQuantities(QuantityTracking):
	f = open('quantities.txt', 'w')
	print("\nWriting to quantity.txt")
	for data_pair in QuantityTracking:
		f.write(str(data_pair[1]) + "\n")
		print("Writing " + str(data_pair[1]))
	print("Done Editing.\n")
	f.close()
	return
