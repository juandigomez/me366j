from motor import motor
from encoder import encoder
import time

def motorTest():
    motorL = motor("left", [32, 31, 33])
    encoderA = encoder("left", [26, 29],50, motorL)
    
    motorL.pinSetup()
    encoderA.pinSetup()
    
    motorL.setVolt(55)
    
    tnow = time.time()
    
    while (tnow + 3 > time.time() ):
        encoderA.RPMcalc()