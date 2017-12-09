from Adafruit_AMG88xx import Adafruit_AMG88xx
from scipy.interpolate import griddata
from colour import Color
import pygame
import os
import sys
import math
import numpy as np
import time
#import threading
from multiprocessing import Process

class TIC ():
    
    #def __init__(self):
     #   threading.Thread.__init__(self)
        
    def TICstart(self):
        #low range of the sensor (this will be blue on the screen)
        self.MINTEMP = 23

        #high range of the sensor (this will be red on the screen)
        self.MAXTEMP = 32

        #how many color values we can have
        self.COLORDEPTH = 1024

        os.putenv('SDL_FBDEV', '/dev/fb1')
        pygame.init()

        #initialize the sensor
        self.sensor = Adafruit_AMG88xx()

        self.points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
        self.grid_x, self.grid_y = np.mgrid[0:7:32j, 0:7:32j]

        #sensor is an 8x8 grid so lets do a square
        height = 240
        width = 240

        #the list of colors we can choose from
        blue = Color("indigo")
        colors = list(blue.range_to(Color("red"), self.COLORDEPTH))

        #create the array of colors
        self.colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

        self.displayPixelWidth = width / 30
        self.displayPixelHeight = height / 30

        self.lcd = pygame.display.set_mode((width, height))

        self.lcd.fill((255,0,0))

        pygame.display.update()
        pygame.mouse.set_visible(False)

        self.lcd.fill((0,0,0))
        pygame.display.update()

        #let the sensor initialize
        time.sleep(.1)
        
        #some utility functions
    def constrain(self,val, min_val, max_val):
        return min(max_val, max(min_val, val))

    def map(self,x, in_min, in_max, out_min, out_max):
      return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def cam(self):
                    #read the pixels
        #while(1):
                pixels = self.sensor.readPixels()
                pixels = [self.map(p, self.MINTEMP, self.MAXTEMP, 0, self.COLORDEPTH - 1) for p in pixels]
                
                #perdorm interpolation
                bicubic = griddata(self.points, pixels, (self.grid_x, self.grid_y), method='cubic')
                
                #draw everything
                for ix, row in enumerate(bicubic):
                        for jx, pixel in enumerate(row):
                                pygame.draw.rect(self.lcd, self.colors[self.constrain(int(pixel), 0, self.COLORDEPTH- 1)], (self.displayPixelHeight * ix, self.displayPixelWidth * jx, self.displayPixelHeight, self.displayPixelWidth))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            sys.exit()
                pygame.display.update()
    
    def run(self):
        #threadLock.acquire()
        self.cam()
        #threadLock.release()

if __name__ == '__main__':
    tic = Process(target = cam, args =() )
    tic.start()
    tic.join()