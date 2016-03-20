#	Control Logic File for Capstone Project Group 25 Spring 2016
#   Authors: Ben Hieltjes, Noel Barron, Luke Mulder 
#   Initial Release: March 2016
#   Python Version 3.X

import RPi.GPIO as GPIO # Raspberry Pi GPIO interface library
from time import sleep # Sleep Command available

# Define GPIO pin associations (Switch-based Ctrl)
Pump = 5
AlcoholServo = 37
Mix1 = 40
Mix2 = 38
Mix3 = 36
Mix4 = 32
Mix5 = 26
Mix6 = 24
MixMotor = 8
MixSolValve = 32

# Define Remaining GPIO pin associations
Camera = 25 # <-- How to control??
Water = 7 # <-- Different from mixer sys or is water in one of the bottles?
StepperMotor = 12 # <-- How do we control this motor?

# Define Time Constants <-- this might not be required if we use camera
time_for_one_shot = 5
sol_valve_on_time = 8
water_on_time = 5

# Configure and Initialize GPIO Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Pump, GPIO.OUT)
GPIO.output(Pump, GPIO.LOW)
GPIO.setup(AlcoholServo, GPIO.OUT)
GPIO.output(AlcoholServo, GPIO.LOW)
GPIO.setup(Mix1, GPIO.OUT)
GPIO.output(Mix1, GPIO.LOW)
GPIO.setup(Mix2, GPIO.OUT)
GPIO.output(Mix2, GPIO.LOW)
GPIO.setup(Mix3, GPIO.OUT)
GPIO.output(Mix4, GPIO.LOW)
GPIO.setup(Mix4, GPIO.OUT)
GPIO.output(Mix4, GPIO.LOW)
GPIO.setup(Mix5, GPIO.OUT)
GPIO.output(Mix5, GPIO.LOW)
GPIO.setup(Mix6, GPIO.OUT)
GPIO.output(Mix6, GPIO.LOW)
GPIO.setup(MixMotor, GPIO.OUT)
GPIO.output(MixMotor, GPIO.LOW)
GPIO.setup(MixSolValve, GPIO.OUT)
GPIO.output(MixSolValve, GPIO.LOW)
GPIO.setup(Water, GPIO.OUT)
GPIO.output(Water, GPIO.LOW)

GPIO.setup(Carousel, GPIO.OUT)
GPIO.output(Carousel, GPIO.LOW)
GPIO.setup(Camera, GPIO.IN) # Not sure if more setup is needed for input pin(s)

# Root function for pouring a drink
def MakeDrink(drinkID):
	# master function content here
	return
	
# Function sends the GPIO output signal to actuate a servo
# @Param pin: The GPIO signal to send
# @Param percent_shot: Amount of liquid to dispense. [0,1] where 1 corresponds to a full shot
def DispenseAlcohol(pin,percent_shot):
	if (percent_shot < 0 or percent_shot > 1):
		print("Invalid Quantity in DispenseAlcohol Func")
	elif (pin != AlcoholServo1 or pin != AlcoholServo2):
		print("Invalid Pin in DispenseAlcohol Func")
	else:
		GPIO.output(pin, GPIO.HIGH)
		sleep(time_for_one_shot*percent_shot) # Assuming Linear Relation
		GPIO.output(pin, GPIO.LOW)
	return
	
# Function sends the GPIO output signal to actuate a servo
# @Param pin: The GPIO signal to send
# @Param mL: Amount of liquid to dispense in mL
def DispenseMix(pin,mL):
	if (mL < 0 or mL > 500):
		print("Invalid Quantity in DispenseMix Func")
	elif (pin != Mix1 or pin != Mix2 or pin != Mix3 or pin != Mix4 or pin != Mix5 or pin != Mix6 or pin != Mix7 or pin != Mix8):
		print("Invalid Pin in DispenseMix Func")
	else:
		GPIO.output(pin, GPIO.HIGH)
		# We need to test to see how long a mL takes to dispense. 0.02s for now.
		sleep(0.02*mL)
		GPIO.output(pin, GPIO.LOW)
	return
		
# Function acutates the mixing motor
# @Param mixTime: Time (s) to activate the mixing motor
def MixDrink(mixTime):
	if (mixTime < 0 or mixTime > 60):
		print("Invalid mixTime")
	else:
		GPIO.output(mixPin, GPIO.HIGH)
		sleep(mixTime)
		GPIO.output(MixPin, GPIO.LOW)
	return
		
# Function to open the solenoid valve between mixing and dispensing
def SolValveCycle():
	GPIO.output(SolValve, GPIO.HIGH)
	sleep(sol_valve_on_time)
	GPIO.output(SolValve, GPIO.LOW)
	return

# Function dispenses water to flush the system
def RinseCycle():
	GPIO.output(Water, GPIO.HIGH)
	sleep(water_on_time)
	GPIO.output(Water, GPIO.LOW)
	SolValveCycle()
	return

#	
# TODO: Carousel Motor Function
#
