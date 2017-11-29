# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:54:26 2017

@author: Michael Personal
"""
class motor:
    
	def __init__(self, name, pins):
		self.name = name
		self.pins = pins
		self.speedPin = pins[0]	#define pin that determines speed
		self.dirPin1 = pins[1]	#define 1st pin that determines direction
		self.dirPin2 = pins[2]	#define 2nd pin that determines direction

	def pinSetup(self):		
		GPIO.setup(self.speedPin, GPIO.OUT)    #motor speed pin
		GPIO.setup(self.dirPin1, GPIO.OUT)    #motor dir1 pin
		GPIO.setup(self.dirPin2, GPIO.OUT)    #motor dir2 pin
		self.my_pwm = GPIO.PWM(self.speedPin, 100)	#creates pwm object
		self.my_pwm.start(0)	# sets speed value based on duty cycle

        
	def setVolt(self, speed):
		self.voltNum = speed
		self.baseValue = 5
		self.duty = abs(100*self.voltNum/self.baseValue) #creates duty cycle based on input Voltage value
		self.sendPower()
	
	def sendPower():
		if(self.voltNum != 0):
			if(self.voltNum > 0):	#set direction
				GPIO.output(self.dirPin1, True)
				GPIO.output(self.dirPin2, False)
			else:
				GPIO.output(self.dirPin1, False)
				GPIO.output(self.dirPin2, True)
				
		else:	#speed is zero
			GPIO.output(self.dirPin1, False)
			GPIO.output(self.dirPin2, False)
		
		self.my_pwm.ChangeDutyCycle(self.duty)
