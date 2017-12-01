import time
from motor import motor
import RPi.GPIO as GPIO

class encoder:
	
	def __init__(self, name, pins, asgnSpeed, mot):
		self.mot = mot
		self.name = name
		self.clk = pins[0]	#encoder pin1
		self.dt = pins[1]	#encoder pin2
		self.count = 0		#number of counts on encoder
		self.start = [False, False]
		self.asgnSpeed = asgnSpeed
		self.RPM = 0
	
	def pinSetup(self):
		GPIO.setup(self.clk, GPIO.IN)
		GPIO.setup(self.dt, GPIO.IN)
		
	def setSpeed(self, speed):
                self.asgnSpeed = speed
                self.mot.setVolt(speed)
	
	def increment(self):
		if (self.start[0] == False):	#initializes clkLastState
			self.clkLastState = GPIO.input(self.clk)
			self.start[0] = True
			self.i=0
			
		clkState = GPIO.input(self.clk)		#set clock values
		dtState = GPIO.input(self.dt)
		
		if clkState != self.clkLastState:	#detect hall effect pulses
			if dtState != clkState:
				self.count += 0.5		#detect direction of hall effect pulse
			else:
				self.count -= 0.5
                self.clkLastState = clkState	#reset last clockstate
                self.i += 1
				
	def RPMcalc(self):	#since RPMcalc invokes increment and regulateSpeed, only RPMcalc needs to be invoked on each loop
		self.increment()
		tElapse = 0.1		#time for RPM calculation
		countsPerRev = 180	#number of pulses per revolution of output shaft
		if (self.start[1] == False):	#begin counting
			self.countRef = self.count
			self.start[1] = True
			self.tnow  = time.time()
		
		elif (time.time() - self.tnow  >= tElapse):	#if enough time elapsed
			self.RPM = (self.count - self.countRef)*60/countsPerRev/(time.time() - self.tnow)
			self.start[1] = False
			self.regulateSpeed()
			
	def regulateSpeed(self):
		self.speedInc = self.asgnSpeed - self.RPM
		if(self.mot.voltNum + self.speedInc > 0):
                    self.mot.setVolt(min(self.speedInc/2 + self.mot.voltNum , self.mot.baseValue))
                else:
                    self.mot.setVolt(max(self.speedInc/2 + self.mot.voltNum, -self.mot.baseValue))
#                print(self.count)