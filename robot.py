from motor import motor
from encoder import encoder
from proximity import psensor
import time
from thread import start_new_thread

class robot:
    
    def __init__(self, motorA, motorB, encoderA, encoderB, proxSensA, proxSensB, proxSensC):
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
    
    def pinSetup(self):
        self.motorA.pinSetup()
        self.motorB.pinSetup()
        self.encoderA.pinSetup()
        self.encoderB.pinSetup()
        self.proxSensA.pinSetup()
        self.proxSensB.pinSetup()
        self.proxSensC.pinSetup()
    
    def runThread(self):
        dirstate = rob.lastDir
        countstate = rob.dirCount
        self.checkNear()
        if (dirstate != self.lastDir or countstate != self.dirCount):
            ctime = time.time()
            while(ctime > time.time() + 1):
                self.checkNear()
                self.direct("forward", 50)
            self.direct(rob.lastDir, 50)
        
            
        self.direct("forward", 50)
       
    def direct(self, direction, RPM):
        if direction == "forward" :
            self.motorA.setSpeed(RPM)
            self.motorB.setSpeed(-RPM)
        elif direction == "backward" :
            self.motorA.setSpeed(-RPM)
            self.motorB.setSpeed(RPM)
        elif direction == "left":
            self.motorA.setSpeed(-RPM)
            self.motorB.setSpeed(-RPM)
	    self.turn(direction, RPM)
        elif direction == "right":
            self.motorA.setSpeed(RPM)
            self.motorB.setSpeed(RPM)
	    self.turn(direction, RPM)
	elif direction == "stop":
            self.motorA.setSpeed(0)
            self.motorB.setSpeed(0)
	
    def turn(self, direction, RPM):
        if direction == "right":
            self.encoderA.setSpeed(RPM)
            self.encoderB.setSpeed(RPM)
            self.dirCount += 1
            self.lastDir = "right"
            while (self.motorA.voltNum != 0 and self.motorB.voltNum != 0):
                self.encoderA.turn(180*self.whlLen /4/self.diam)
                self.encoderB.turn(180*self.whlLen /4/self.diam)
        elif direction == "left":
            self.encoderA.setSpeed(-RPM)
            self.encoderB.setSpeed(-RPM)
            self.dirCount += 1
            self.lastDir = "left"
            while (self.motorA.voltNum != 0 and self.motorB.voltNum != 0):
                self.encoderA.turn(-180*self.whlLen /4/self.diam)
                self.encoderB.turn(-180*self.whlLen /4/self.diam)
        self.direct("stop", 0)
        self.direct("stop", 0)
    
    def traverse(self):
        dirstate = self.lastDir
        countstate = self.lastDir
        self.checkNear()
        
    
    def checkNear(self):
        if(self.near()):
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

"""

    def pulseScan(self):
            a = self.near(self.proxSensA)
            b = self.near(self.proxSensB)
            c = self.near(self.proxSensC)
            
            if a ==False:
                    self.direct("forward", 50)
            else:
                    if(b == False):
                            if c:
                                    self.direct("left", 50)
                            else:
                                    self.direct("right", 50)
            
    def cornerCheck(self):
            if (self.near(self.proxSensA)):
                    if (!self.near(self.proxSensB)):
                            if (self.near(proxSensC)):
                                    self.direct("left", 50)
                            else:
                                    if (
"""