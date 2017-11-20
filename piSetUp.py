# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 22:08:59 2017

@author: Michael Personal
"""
# =============================================================================
# =============================================================================
from motor import motor
import time

def piSetUp():
	
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)
	
	motorL = motor("left", [29, 31])
	motorR = motor("right", [33, 35]])
	motorL.pinSetup()
	motorR.pinSetup()
	motorL.setVolt(5)
	motorR.setVolt(2.5)
	timer.sleep(10)
	
	GPIO.cleanup()
	
	
	"""
    GPIO.setup(11, GPIO.OUT)    #motorA speed pin
    GPIO.setup(13, GPIO.OUT)    #motorA dir1 pin
    GPIO.setup(15, GPIO.OUT)    #motorA dir2 pin
    
    GPIO.setup(12, GPIO.OUT)    #motorB speed pin
    GPIO.setup(16, GPIO.OUT)    #motorB dir1 pin
    GPIO.setup(18, GPIO.OUT)    #motorB dir2 pin
    
	"""
if __name__== "__main__" :
	piSetUp()
