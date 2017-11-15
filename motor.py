# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:54:26 2017

@author: Michael Personal
"""
$ sudo python

import RPi.GPIO as GPIO

class motor:
    
	def __init__(self, name, pins):
		self.name = name
		self.pins = pins
		self.speedPin = pins[0]	#define pin that determines speed
		self.dirPin1 = pins[1]	#define 1st pin that determines direction
		self.dirPin2 = pins[2]	#define 2nd pin that determines direction
		
        
	def setSpeed(self, speed):
		self.voltNum = speed
		self.baseValue = 3.3
		self.duty = abs(self.voltNum/self.baseValue) #creates duty cycle based on input Voltage value
		self.sendPower()
		
	def pinSetup(self):		
		GPIO.setup(self.speedPin, GPIO.OUT)    #motor speed pin
		GPIO.setup(self.dirPin1, GPIO.OUT)    #motor dir1 pin
		GPIO.setup(self.dirPin2, GPIO.OUT)    #motor dir2 pin
	
	def sendPower():
		if(self.voltNum != 0):
			if(self.voltNum > 0):	#set direction
				GPIO.output(self.dirPin1, True)
				GPIO.output(self.dirPin2, False)
			else:
				GPIO.output(self.dirPin1, False)
				GPIO.output(self.dirPin2, True)
				
			my_pwm = GPIO.PWM(self.speedPin, 100)	#creates pwm object
			my_pwm.start(self.duty)	# sets speed value based on duty cycle
		
		else:	#speed is zero
			GPIO.output(self.dirPin1, False)
			GPIO.output(self.dirPin2, False)
			GPIO.output(self.speedPin, False)

			
			