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
from proximity import psensor
from Adafruit_AMG88xx import Adafruit_AMG88xx
from scipy.interpolate import griddata
from colour import Color
from TIC import TIC
import time
import sys
import pygame
import math
import numpy as np

def piSetUp():
        
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)
	
	TIC1 = TIC()
	TIC1.TICstart()

	motorL = motor("left", [32, 31, 33])
        encoderA = encoder("left", [26, 29], 50, motorL)
        
        motorR = motor("right", [35, 36, 37])
        encoderB = encoder("left", [38, 40], 50, motorR)
        
        proxSensA= psensor("Front",[16,18])
        proxSensB= psensor("Left",[12,22])
        proxSensC= psensor("Right",[7,13])
        
        rob = robot(motorL, motorR, encoderA, encoderB, proxSensA, proxSensB, proxSensC)
        rob.pinSetup()
	tnow = time.time()
	"""time.time() < tnow +3"""
        
	while(1):
            n=0
            rob.obsDetect()
            done = False
            if rob.distanceA < 50:
                while rob.distanceA < 50:
                    rob.obsDetect()
                    rob.direct("backward", 50)
                    n+=1
            else:
                print(rob.distanceA)
                rob.direct("forward", 50)
            """rob.direct("forward", 50)
            rob.runLoop()
            proxSensA.measure()
            rob.obsDetect()
            print(rob.distanceA)
            if rob.distanceA < 15:
                while n < 50000:
                    rob.direct("backward", 50)
                    n+=1"""
            TIC1.cam()
            

#        tnow = time.time()
#	while(time.time() < tnow +3):
#            rob.direct("backward", 50)
            #rob.obsDetect()
#        tnow = time.time()
#	while(time.time() < tnow +3):
#            rob.direct("left", 50)
            #rob.obsDetect()
#        tnow = time.time()
#	while(time.time() < tnow +3):
#            rob.direct("right", 50)
            #rob.obsDetect()
            
	#GPIO.cleanup()
	
if __name__== "__main__" :
        import RPi.GPIO as GPIO
	try:
            piSetUp()
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()
