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
import time
import sys
import pygame
import os
import math
import numpy as np

#low range of the sensor (this will be blue on the screen)
MINTEMP = 26

#high range of the sensor (this will be red on the screen)
MAXTEMP = 32

#how many color values we can have
COLORDEPTH = 1024

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

#initialize the sensor
sensor = Adafruit_AMG88xx()

points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

#sensor is an 8x8 grid so lets do a square
height = 240
width = 240

#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))

#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

displayPixelWidth = width / 30
displayPixelHeight = height / 30

lcd = pygame.display.set_mode((width, height))

lcd.fill((255,0,0))

pygame.display.update()
pygame.mouse.set_visible(False)

lcd.fill((0,0,0))
pygame.display.update()

#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#let the sensor initialize
time.sleep(.1)

def piSetUp():
    
        sensor = Adafruit_AMG88xx()
	
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)

	motorL = motor("left", [32, 31, 33])
        encoderA = encoder("left", [26, 29], 50, motorL)
        
        motorR = motor("right", [35, 36, 37])
        encoderB = encoder("left", [38, 40], 50, motorR)
        
        proxSensA= psensor("Front",[16,18])
        proxSensB= psensor("Left",[12,22])
        proxSensC= psensor("Right",[7,13])
        
        rob = robot(motorL, motorR, encoderA, encoderB, proxSensA, proxSensB, proxSensC)
        rob.pinSetup()
        motorL.setVolt(50)
        motorR.setVolt(50)
	tnow = time.time()
	"""time.time() < tnow +3"""
	while(1):
            n=0
            rob.direct("forward", 50)
            rob.runLoop()
            rob.obsDetect()
            if (rob.distanceA < 15):
                while n < 50000:
                    rob.direct("backward", 50)
                    n+=1
            #read the pixels
            pixels = sensor.readPixels()
            pixels = [map(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
            
            #perdorm interpolation
            bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
            
            #draw everything
            for ix, row in enumerate(bicubic):
                    for jx, pixel in enumerate(row):
                            pygame.draw.rect(lcd, colors[constrain(int(pixel), 0, COLORDEPTH- 1)], (displayPixelHeight * ix, displayPixelWidth * jx, displayPixelHeight, displayPixelWidth))
            
            pygame.display.update()

        print encoderA.counts
        print encoderB.counts
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
