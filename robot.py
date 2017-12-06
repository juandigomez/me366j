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
            self.motorB.setSpeed(RPM)
        elif direction == "backward" :
            self.motorA.setSpeed(-RPM)
            self.motorB.setSpeed(-RPM)
        elif direction == "left":
            self.motorA.setSpeed(-RPM)
            self.motorB.setSpeed(RPM)
			self.turn(direction, RPM)
        elif direction == "right":
            self.motorA.setSpeed(RPM)
            self.motorB.setSpeed(-RPM)
			self.turn(direction, RPM)
	
	def turn(self, direction, RPM):
		if direction == "right":
			while (motorA.voltNum != 0 && motorB.voltNum != 0):
				self.encoderA.turn(-180*self.whlLen /4/self.diam)
				self.encoderB.turn(180*self.whlLen /4/self.diam)
		else:
			while (motorA.voltNum != 0 && motorB.voltNum != 0):
				self.encoderA.turn(180*self.whlLen /4/self.diam)
				self.encoderB.turn(-180*self.whlLen /4/self.diam)

			
	def near(self, prox):
		threshold = 20
		if (prox.measure < threshold):
			return True
		else:
			return False
			
	def pulseScan(self):
		a = self.near(self.proxSensA)
		b = self.near(self.proxSensB)
		c = self.near(self.proxSensC)
		
		if !a:
			self.direct("forward", 50)
		else:
			if(!b):
				if c:
					self.direct("left", 50)
				else:
		
	def cornerCheck(self):
		if (self.near(self.proxSensA)):
			if (!self.near(self.proxSensB)):
				if (self.near(proxSensC)):
					self.direct("left", 50)
				else:
					if (
            
    def obsDetect(self):
        self.distanceA = self.proxSensA.measure()
        self.distanceB = self.proxSensB.measure()
        self.distanceC = self.proxSensC.measure()

    
    def runLoop(self):
        self.encoderA.RPMcalc()
        self.encoderB.RPMcalc()
