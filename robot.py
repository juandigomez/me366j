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
#        self.proxSensB = proxSensB
#        self.proxSensC = proxSensC
    
    def pinSetup(self):
        self.motorA.pinSetup()
        self.motorB.pinSetup()
        self.encoderA.pinSetup()
        self.encoderB.pinSetup()
        self.proxSensA.pinSetup()
        
    def direct(self, direction, RPM):
        if direction == "forward" :
            self.encoderA.setSpeed(RPM)
            self.encoderB.setSpeed(RPM)
        elif direction == "backward" :
            self.encoderA.setSpeed(-RPM)
            self.encoderB.setSpeed(-RPM)
        elif direction == "left":
            self.encoderA.setSpeed(-RPM)
            self.encoderB.setSpeed(RPM)
        elif direction == "right":
            self.encoderA.setSpeed(RPM)
            self.encoderB.setSpeed(-RPM)
            
    def obsDetect(self):
        distance = self.proxSensA.measure()
        print(distance)
        
    """def swerve(self):
        obs = self.obsDetect()
        print(obs)
        if obs < 15:
            self.direct("backward", 50)"""

    
    def runLoop(self):
        self.encoderA.RPMcalc()
        self.encoderB.RPMcalc()