def straightRun():

	GPIO.setmode(GPIO.BOARD)
	
	motorL = motor("left", [32, 31, 33])
        encoderA = encoder("left", [26, 29], 50, motorL)
            
        motorR = motor("right", [35, 36, 37])
        encoderB = encoder("left", [38, 40], 50, motorR)
	
	proxSensA= psensor("Front",[16,18], 50)
        proxSensB= psensor("Left",[12,22], 35)
        proxSensC= psensor("Right",[7,13], 35)
	
	rob = robot(motorL, motorR, encoderA, encoderB, proxSensA, proxSensB, proxSensC)
        rob.pinSetup()
	
	while(1):
            rob.direct("forward", 50)
	
		
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
            straightRun()
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()