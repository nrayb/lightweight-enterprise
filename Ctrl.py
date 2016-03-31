#	Control Logic File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016
#   Python Version 3.X

import RPi.GPIO as GPIO # Raspberry Pi GPIO interface library
from time import sleep # Sleep Command available

# Define GPIO pin associations (Switch-based Ctrl)
PumpPin = 5
AlcoholServoPin = 37
ColaPin = 40
LimeJuicePin = 38
SodaWaterPin = 32
OJPin = 24
WaterPin = 7
MixMotorPin = 8
MixSolValvePin = 32


# Define Remaining GPIO pin associations
Camera = 25 # <-- How to control??
StepperMotor = 12 # <-- How do we control this motor?

# Define Time Constants (s) <-- this might not be required if we use camera
time_for_one_shot = 5
sol_valve_on_time = 8
water_rinse_time = 5
time_to_dispense_mL = 0.02

# Configure and Initialize GPIO Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PumpPin, GPIO.OUT)
GPIO.output(PumpPin, GPIO.LOW)
GPIO.setup(AlcoholServoPin, GPIO.OUT)
GPIO.output(AlcoholServoPin, GPIO.LOW)
GPIO.setup(ColaPin, GPIO.OUT)
GPIO.output(ColaPin, GPIO.LOW)
GPIO.setup(LimeJuicePin, GPIO.OUT)
GPIO.output(LimeJuicePin, GPIO.LOW)
GPIO.setup(LemonJuicePin, GPIO.OUT)
GPIO.output(LemonJuicePin, GPIO.LOW)
GPIO.setup(SodaWaterPin, GPIO.OUT)
GPIO.output(SodaWaterPin, GPIO.LOW)
GPIO.setup(SimpleSyrupPin, GPIO.OUT)
GPIO.output(SimpleSyrupPin, GPIO.LOW)
GPIO.setup(OJPin, GPIO.OUT)
GPIO.output(OJPin, GPIO.LOW)
GPIO.setup(MixMotorPin, GPIO.OUT)
GPIO.output(MixMotorPin, GPIO.LOW)
GPIO.setup(MixSolValvePin, GPIO.OUT)
GPIO.output(MixSolValvePin, GPIO.LOW)
GPIO.setup(WaterPin, GPIO.OUT)
GPIO.output(WaterPin, GPIO.LOW)

# How to control stepper motor? Need these GPIO config statements as well
GPIO.setup(Camera, GPIO.IN) # Not sure if more setup is needed for input pin(s)

# Root function for pouring a drink
def MakeDrink(drinkID):
	# master function content here
	
	# Print Recipe. For Debug.
	Master.printRecipe(drinkNo)
	
	# Decode drink and pour contents into mixing chamber
	for ingredient in Drinklist.drinks[drinkID]:			
		if ingredient[0] == "Alcohol":
			# Alcohol ingredient detected
			print("Dispensing " + str(ingredient[2]) + "mL of " + ingredient[1])
			DispenseAlcohol(ingredient[1],ingredient[2])
		elif ingredient[0] == "Mixer":
			# Mixer ingredient detected
			print("Dispensing " + str(ingredient[2]) + "mL of " + ingredient[1])			
			DispenseMix(ingredient[1],ingredient[2])
		elif ingredient[0] == "None":
			# Skip over empty ingredients. Only happens in case of custom drink.
			continue
		else:
			# Shouldn't be here
			print("ERROR: Ingredient parsing. Ingredient was: " + ingredient)
			return
			
	MixDrink(10) # Mix for 10s
	MixChamberValve(True) # Dispense into cup
	sleep(30) # Allow 30s for dispensing and removal of cup
	RinseCycle() # Rinse chamber
	MixChamberValve(False) # Close dispenal valve for next drink
	
	return
	
# Function sends the GPIO output signal to actuate a servo
# @Param pin: The GPIO signal to send
# @Param mL: Amount of liquid to dispense
def DispenseAlcohol(AlcoholType, mL):	

	if (mL < 0 or mL > 500):
		print("ERROR: Invalid Quantity in DispenseAlcohol Func. Input of " + str(mL) + "mL")
		return
		
	# Identify required stepper motor commands
	if AlcoholType == "Vodka":
		# Place required parameter assignmenet here for stepper motor control
	elif AlcoholType == "Gin":
	
	elif AlcoholType == "Rum":
	
	elif AlcoholType == "Whiskey":
	
	else:
		print("ERROR: Invalid type of alcohol detected. AlcoholType was: " + AlcoholType)
		return
	
	# Rotate stepper motor
	RotateCarousel()
	
	
	GPIO.output(AlcoholServoPin, GPIO.HIGH)
	# We need to test to see how long a mL takes to dispense. 0.02s for now.
	# Can replace with system feedback when applicable
	sleep(time_to_dispense_mL*mL)
	GPIO.output(AlcoholServoPin, GPIO.LOW)
	return
	
# Function sends the GPIO output signal to actuate a servo
# @Param pin: The GPIO signal to send
# @Param mL: Amount of liquid to dispense in mL
def DispenseMix(MixType, mL):

	# Find correct pin
	if MixType == "Cola":
		mixerpin = ColaPin
	elif MixType == "Lime Juice":
		mixerpin = LimeJuicePin
	elif MixType == "Orange Juice":
		mixerpin = OJPin
	elif MixType == "Soda Water":
		mixerpin == SodaWaterPin
	else:
		# Unable to Identify Correct Mixer Pin
		print("ERROR: Unable to Identify Correct Mixer Pin. Argument MixType was:" + MixType)
		return
		
	# Verify quantity is valid
	if (mL < 0 or mL > 500):
		print("ERROR: Invalid Quantity in DispenseMix Func. Input of " + str(mL) + "mL")
		return
	
	GPIO.output(mixerpin, GPIO.HIGH) # Open correct valve
	GPIO.output(PumpPin, GPIO.HIGH) # Turn on Pump
	# We need to test to see how long a mL takes to dispense. 0.02s for now.
	# Can replace with system feedback when applicable
	sleep(time_to_dispense_mL*mL)
	GPIO.output(PumpPin, GPIO.LOW) # Turn off Pump. Possibly put a delay before closing the valve if the pump doesn't stop immediately.
	GPIO.output(mixerpin, GPIO.LOW) # Close valve
	
	return
		
# Function acutates the mixing motor
# @Param mixTime: Time (s) to activate the mixing motor
def MixDrink(mixTime):
	if (mixTime < 0 or mixTime > 60):
		print("ERROR: Invalid mixTime of " + str(mixTime))
	else:
		GPIO.output(MixPin, GPIO.HIGH)
		sleep(mixTime)
		GPIO.output(MixPin, GPIO.LOW)
	return

# Function actuates the pump
# @Param boolean: actuation command to motor
def PumpOn(boolean):
	if boolean == True:
		GPIO.output(PumpPin, GPIO.HIGH)
	elif boolean == False:
		GPIO.output(PumpPin, GPIO.LOW)
	else:
		print("ERROR: Invalid Argument to Pump")
		GPIO.output(PumpPin, GPIO.LOW) # Off by default
	return
		
# Function to open the solenoid valve between mixing and dispensing
# @Param open: actuation command to mixing chamber valve
def MixChamberValve(open):
	if open == True:
		GPIO.output(SolValvePin, GPIO.HIGH)
	elif open == False:
		GPIO.output(SolValvePin, GPIO.LOW)
	else:
		print("ERROR: Invalid argument to mixchambervalve")
		GPIO.output(SolValvePin, GPIO.LOW) # Valve closed by default
	return

# Function dispenses water to flush the system
def RinseCycle():
	GPIO.output(WaterPin, GPIO.HIGH) # Open Water Valve
	GPIO.output(PumpPin, GPIO.HIGH) # Turn on Pump
	sleep(water_rinse_time)
	GPIO.output(PumpPin, GPIO.LOW) # Turn off Pump. Possibly put a delay before closing the valve if the pump doesn't stop immediately.
	GPIO.output(WaterPin, GPIO.LOW) # Close Water Valve
	return

# Function to rotate carousel to required position
# @Param ???: <description>
def RotateCarousel():
	# TODO
	return
