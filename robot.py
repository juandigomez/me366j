from motor import motor
from encoder import encoder
from proximity import psensor
import time

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
    
    def pinSetup(self):
        self.motorA.pinSetup()
        self.motorB.pinSetup()
        self.encoderA.pinSetup()
        self.encoderB.pinSetup()
        self.proxSensA.pinSetup()
        self.proxSensB.pinSetup()
        self.proxSensC.pinSetup()
        
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
            while (self.motorA.voltNum != 0 and self.motorB.voltNum != 0):
                self.encoderA.turn(180*self.whlLen /4/self.diam)
                self.encoderB.turn(180*self.whlLen /4/self.diam)
        else:
            self.encoderA.setSpeed(-RPM)
            self.encoderB.setSpeed(-RPM)
            while (self.motorA.voltNum != 0 and self.motorB.voltNum != 0):
                self.encoderA.turn(-180*self.whlLen /4/self.diam)
                self.encoderB.turn(-180*self.whlLen /4/self.diam)
        self.encoderA.setSpeed(0)
        self.encoderB.setSpeed(0)
			
    def near(self, prox):
            threshold = 20
            if (self.proxSensA.measure < threshold):
                    self.direct(0, "stop")
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