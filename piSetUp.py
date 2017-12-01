# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 22:08:59 2017

@author: Michael Personal
"""
# =============================================================================
# =============================================================================
from motor import motor
from encoder import encoder
from robot import robot
import time

def piSetUp():
	
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)

	motorL = motor("left", [32, 31, 33])
        encoderA = encoder("left", [26, 29], 50, motorL)
        
        motorR = motor("right", [35, 36, 37])
        encoderB = encoder("left", [38, 40], 50, motorR)
        
        proxSensA=3
        proxSensB=3
        proxSensC=3
        
        rob = robot(motorL, motorR, encoderA, encoderB, proxSensA, proxSensB, proxSensC)
        rob.pinSetup()
        motorL.setVolt(50)
        motorR.setVolt(50)
	tnow = time.time()
	while(time.time() < tnow +3):
            rob.direct("forward", 50)
        tnow = time.time()
	while(time.time() < tnow +3):
            rob.direct("backward", 50)
        tnow = time.time()
	while(time.time() < tnow +3):
            rob.direct("left", 50)
        tnow = time.time()
	while(time.time() < tnow +3):
            rob.direct("right", 50)
            
	GPIO.cleanup()
	
if __name__== "__main__" :
	piSetUp()
