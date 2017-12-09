# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 22:08:59 2017

@author: Michael Personal
"""
# =============================================================================
# =============================================================================

def piSetUp():

	GPIO.setmode(GPIO.BOARD)
	
	TIC1 = TIC()
	TIC1.TICstart()

	motorL = motor("left", [32, 31, 33])
        encoderA = encoder("left", [26, 29], 50, motorL)
        
        motorR = motor("right", [35, 36, 37])
        encoderB = encoder("left", [38, 40], 50, motorR)
        
        proxSensA= psensor("Front",[16,18], 50)
        proxSensB= psensor("Left",[12,22], 35)
        proxSensC= psensor("Right",[7,13], 35)
        
        rob = robot(motorL, motorR, encoderA, encoderB, proxSensA, proxSensB, proxSensC)
        rob.pinSetup()
        
        tnow = time.time()
        while(1):
            rob.run()
            TIC1.run()
        
        #TIC1.start()
        #rob.start()
        #rob.join()
        #TIC1.join()
        #while(1):
         #   newThread
        #while(tnow + 60 > time.time() ):
            
        
""" 
        rob.direct("forward", 50)
        tnow = time.time()
        while(tnow + 60 > time.time()):
            dirstate = rob.lastDir
            countstate = rob.dirCount
            rob.checkNear()
            if (dirstate != rob.lastDir or countstate != rob.dirCount):
                ctime = time.time()
                while(ctime > time.time() + 1):
                    rob.checkNear()
                    rob.direct("forward", 50)
                rob.direct(rob.lastDir, 50)
                rob.dirCount = 2
            
                
            rob.direct("forward", 50)
"""

if __name__== "__main__" :
        from motor import motor
        from encoder import encoder
        from robot import robot
        from proximity import psensor
        from TIC import TIC
        import time
        import pygame
        import sys
        import RPi.GPIO as GPIO
        from thread import start_new_thread
        #from multiprocessing import Process
	try:
            piSetUp()
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()
