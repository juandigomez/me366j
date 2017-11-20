# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:54:26 2017

@author: Michael Personal
"""
class motor:
    
	def __init__(self, name, pins):
		self.name = name
		self.pins = pins
		self.dirPin1 = pins[0]	#define 1st pin that determines direction
		self.dirPin2 = pins[1]	#define 2nd pin that determines direction

	def pinSetup(self):		
		GPIO.setup(self.dirPin1, GPIO.OUT)    #motor dir1 pin
		GPIO.setup(self.dirPin2, GPIO.OUT)    #motor dir2 pin	
		my_pwm1 = GPIO.PWM(self.dirPin1, 100) #enables dir1 pin for PWM with frequency 100
		my_pwm2 = GPIO.PWM(self.dirPin2, 100) #enables dir2 pin for PWM with frequency 100
		my_pwm1.start(0)	# sets speed value based on duty cycle
		my_pwm2.start(0)	# sets speed value based on duty cycle
        
	def setVolt(self, speed):
		self.voltNum = speed
		self.baseValue = 5
		self.duty = abs(100*self.voltNum/self.baseValue) #creates duty cycle based on input Voltage value
		self.sendPower()
	
	def sendPower():
		if(self.voltNum != 0):
			if(self.voltNum > 0):	#set direction
				my_pwm1.ChangeDutyCycle(self.duty)	# sets speed value based on duty cycle
				my_pwm2.ChangeDutyCycle(0)	# sets speed value based on duty cycle
			else:
				my_pwm1.ChangeDutyCycle(0)
				my_pwm2.ChangeDutyCycle(self.duty)
		
		else:	#speed is zero
			my_pwm1.ChangeDutyCycle(0)
			my_pwm2.ChangeDutyCycle(0)

			
			
