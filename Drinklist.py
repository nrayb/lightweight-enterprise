#	Drinklist File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016

# Top Array. 3 levels of list. Each drink has a list of ingredients. Each ingredient has a list of labels.
drinks = []

# Assumed Alcohols are: Vodka, Rum, Gin, and Whiskey
# Assumed Mixers are: Cola, Lime, OJ, Lemon, Soda Water, Simple Syrup

# DrinkNo Correspondances
RC = 0 # Rum and Coke
SD = 1 # Screwdriver
WS = 2 # Whiskey Sour
GR = 3 # Gin Rickey
DAQ = 4 # Daiquiri
TC = 5 # Tom Collins
GM = 6 # Gimlet
LI = 7 # Long Island Ice Tea

# Format for Alcohol: ("Alcohol", "<Type>", <# shots>)
# Format for Mixer: ("Mixer", "<Type>", mL)

drinks.insert(RC,[])
drinks[RC].insert(0, ["Alcohol", "Rum", 1])
drinks[RC].insert(1, ["Mixer", "Cola", 250])
drinks[RC].insert(2, ["Mixer", "Lime Juice", 45])

drinks.insert(SD,[])
drinks[SD].insert(0, ["Alcohol", "Vodka", 1.5])
drinks[SD].insert(1, ["Mixer", "OJ", 250])

drinks.insert(WS,[])
drinks[WS].insert(0, ["Alcohol", "Whiskey", 2])
drinks[WS].insert(1, ["Mixer", "Lemon Juice", 45])
drinks[WS].insert(2, ["Mixer", "Simple Syrup", 20])

drinks.insert(GR,[])
drinks[GR].insert(0, ["Alcohol", "Gin", 2])
drinks[GR].insert(1, ["Mixer", "Soda Water", 200])
drinks[GR].insert(2, ["Mixer", "Lime Juice", 30])

drinks.insert(DAQ,[])
drinks[DAQ].insert(0, ["Alcohol", "Rum", 2])
drinks[DAQ].insert(1, ["Mixer", "Simple Syrup", 45])
drinks[DAQ].insert(2, ["Mixer", "Lime Juice", 45])

drinks.insert(TC,[])
drinks[TC].insert(0, ["Alcohol", "Gin", 2])
drinks[TC].insert(1, ["Mixer", "Simple Syrup", 30])
drinks[TC].insert(2, ["Mixer", "Lemon Juice", 30])
drinks[TC].insert(3, ["Mixer", "Soda Water", 200])

drinks.insert(GM,[])
drinks[GM].insert(0, ["Alcohol", "Gin", 2])
drinks[GM].insert(1, ["Mixer", "Simple Syrup", 20])
drinks[GM].insert(2, ["Mixer", "Lime Juice", 45])

drinks.insert(LI,[])
drinks[LI].insert(0, ["Alcohol", "Gin", 1])
drinks[LI].insert(1, ["Alcohol", "Vodka", 1])
drinks[LI].insert(2, ["Alcohol", "Rum", 1])
drinks[LI].insert(3, ["Mixer", "Lime Juice", 45])
drinks[LI].insert(4, ["Mixer", "Cola", 135])
