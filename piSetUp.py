# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 22:08:59 2017

@author: Michael Personal
"""
# =============================================================================
# =============================================================================
from motor import motor

def piSetUp():
    
    GPIO.setmode(GPIO.BOARD)
	
	motorL = motor("left", [11, 13, 15])
	motorL.pinSetup()
	motorL.setSpeed(3.3)
	time.sleep(10)
	motor.L.setSpeed(0)
	
	GPIO.cleanup()
	
	
	"""
    GPIO.setup(11, GPIO.OUT)    #motorA speed pin
    GPIO.setup(13, GPIO.OUT)    #motorA dir1 pin
    GPIO.setup(15, GPIO.OUT)    #motorA dir2 pin
    
    GPIO.setup(12, GPIO.OUT)    #motorB speed pin
    GPIO.setup(16, GPIO.OUT)    #motorB dir1 pin
    GPIO.setup(18, GPIO.OUT)    #motorB dir2 pin
    
	"""