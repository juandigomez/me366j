from motor import motor
from encoder import encoder
from proximity import psensor
import time
#import threading
from multiprocessing import Process

class robot:
    
    def __init__(self, motorA, motorB, encoderA, encoderB, proxSensA, proxSensB, proxSensC):
        #threading.Thread.__init__(self)
        self.motorA = motorA
        self.motorB = motorB
        self.encoderA = encoderA
        self.encoderB = encoderB
        self.proxSensA = proxSensA
        self.proxSensB = proxSensB
        self.proxSensC = proxSensC
	self.whlLen = 365.8
	self.diam = 4*25.4
	self.lastDir = "left"
	self.dirCount = 0
	self.frontCheck = False
    
    def pinSetup(self):
        self.motorA.pinSetup()
        self.motorB.pinSetup()
        self.encoderA.pinSetup()
        self.encoderB.pinSetup()
        self.proxSensA.pinSetup()
        self.proxSensB.pinSetup()
        self.proxSensC.pinSetup()
    
    def run(self):
        self.autonomous()
    
    def autonomous(self):
        #while(1):
            dirstate = self.lastDir
            countstate = self.dirCount
            self.checkNear()
            #if (dirstate != self.lastDir or countstate != self.dirCount):
             #   ctime = time.time()
              #  while(ctime > time.time() + 1):
               #     self.checkNear()
                #    self.direct("forward", 50)
                #self.direct(self.lastDir, 50)
        
        
            self.direct("forward", 50)
       
    def direct(self, direction, RPM):
        if direction == "forward" :
            self.motorA.setSpeed(-RPM)
            self.motorB.setSpeed(RPM)
        elif direction == "backward" :
            self.motorA.setSpeed(RPM)
            self.motorA.setSpeed(-RPM)
            self.turn(direction, RPM)
            """if self.frontCheck == False:
                    self.frontCheck = True
                    self.tRef = time.time()
            if (self.tRef + 0.75 > time.time()):
                    self.motorA.setSpeed(RPM)
                    self.motorB.setSpeed(-RPM)                    
            else:
                    self.direct("stop" , 0)
                    self.frontCheck = False
            """
        elif direction == "left":
            self.motorA.setSpeed(RPM)
            self.motorB.setSpeed(RPM)
	    self.turn(direction, RPM)
        elif direction == "right":
            self.motorA.setSpeed(-RPM)
            self.motorB.setSpeed(-RPM)
	    self.turn(direction, RPM)
	elif direction == "stop":
            self.motorA.setSpeed(0)
            self.motorB.setSpeed(0)
	
    def turn(self, direction, RPM):
        tStep = 1.5
        if direction == "backward":
            self.encoderA.setSpeed(RPM)
            self.encoderB.setSpeed(-RPM)
            self.dirCount += 1
            self.lastDir = "right"
            while (self.motorA.voltNum != 0 and self.motorB.voltNum != 0):
                self.encoderA.turn(tStep)#180*self.whlLen /4/self.diam)
                self.encoderB.turn(tStep) 
        if direction == "right":
            self.encoderA.setSpeed(RPM)
            self.encoderB.setSpeed(RPM)
            self.dirCount += 1
            self.lastDir = "right"
            while (self.motorA.voltNum != 0 and self.motorB.voltNum != 0):
                self.encoderA.turn(tStep)#180*self.whlLen /4/self.diam)
                self.encoderB.turn(tStep) #180*self.whlLen /4/self.diam)
        elif direction == "left":
            self.encoderA.setSpeed(-RPM)
            self.encoderB.setSpeed(-RPM)
            self.dirCount += 1
            self.lastDir = "left"
            while (self.motorA.voltNum != 0 and self.motorB.voltNum != 0):
                self.encoderA.turn(tStep) #-180*self.whlLen /4/self.diam)
                self.encoderB.turn(tStep) #-180*self.whlLen /4/self.diam)
        self.direct("stop", 0)
        self.direct("stop", 0)
    
    def traverse(self):
        dirstate = self.lastDir
        countstate = self.lastDir
        self.checkNear()
        
    
    def checkNear(self):
        if(self.near()):
            if self.distanceA < self.proxSensA.threshold:
                self.direct("backward", 50)
                """if self.frontCheck == False:
                    self.frontCheck = True
                    self.tRef = time.time()
                if (self.tRef + 0.75 > time.time()):
                    self.direct("backward", 50)
                else:
                    self.direct("stop" , 0)
                    self.frontCheck = False
                """
            if (self.lastDir == "left"):
                if self.dirCount < 2 :
                    self.direct("left", 50)
                    if self.near():
                        self.direct("right", 50)
                        self.direct("right", 50)
                        self.dirCount = 1
                else:
                    self.dirCount = 0
                    self.direct("right", 50)
                    if self.near():
                        self.direct("left", 50)
                        self.direct("left", 50)
                        self.dirCount = 1
            
            else:
                if self.dirCount < 2 :
                    self.direct("right", 50)
                    if self.near():
                        self.direct("left", 50)
                        self.direct("left", 50)
                        self.dirCount = 1
                else:
                    self.dirCount = 0
                    self.direct("left", 50)
                    if self.near():
                        self.direct("right", 50)
                        self.direct("right", 50)
                        self.dirCount = 1
         			
    def near(self):
            self.obsDetect()
            if (self.distanceA < self.proxSensA.threshold or self.distanceB < self.proxSensB.threshold or self.distanceC < self.proxSensC.threshold ):
                    self.direct("stop", 0)
                    return True
            else:
                    return False
                
    def obsDetect(self):
        self.distanceA = self.proxSensA.measure()
        self.distanceB = self.proxSensB.measure()
        self.distanceC = self.proxSensC.measure()
        
    def runLoop(self):
        self.encoderA.RPMcalc()
        self.encoderB.RPMcalc()

if __name__== '__main__':
    rob = Process(target = autonomous, args = ())
    rob.start()
    rob.join()