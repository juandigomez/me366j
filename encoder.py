import time
from motor import motor

class encoder:
	
	def __init__(self, name, pins, asgnSpeed)
		self.name = name
		self.clk = pins[0]	#encoder pin1
		self.dt = pins[1]	#encoder pin2
		self.count = 0		#number of counts on encoder
		self.start = [False, False]
		self.asgnSpeed = asgnSpeed
		self.RPM = 0
	
	def pinSetup(self)
		GPIO.setup(self.clk, GPIO.IN)
		GPIO.setup(self.dt, GPIO.IN)
	
	def increment(self)
		if (self.start[0] == False):	#initializes clkLastState
			self.clkLastState = GPIO.input(self.clk)
			self.start[0] = True
			
		clkState = GPIO.input(self.clk)		#set clock values
		dtState = GPIO.input(self.dt)
		
		if clkState != self.clkLastState:	#detect hall effect pulses
			if dtState != clkState:
				self.count += 0.5		#detect direction of hall effect pulse
			else:
				self.count -= 0.5
				
		self.clkLastState = clkState	#reset last clockstate
				
	def RPMcalc(self, mot)	#since RPMcalc invokes increment and regulateSpeed, only RPMcalc needs to be invoked on each loop
		self.increment()
		tElapse = 1		#time for RPM calculation
		countsPerRev = 180	#number of pulses per revolution of output shaft
		if (self.start[1] == False):	#begin counting
			self.countRef = self.count
			self.start[1] = True
			self.tnow  = time.time()
		
		else if (time.time() - self.tnow  >= tElapse)	#if enough time elapsed
			self.RPM = (self.count - self.countRef)*60/countsPerRev/(time.time() - self.tnow)
			self.start[1] = False
			self.regulateSpeed(mot)
			
	def regulateSpeed(self, mot)
		self.speedInc = self.asgnSpeed - self.RPM
		mot.setSpeed(self.speedInc + motor.speed)
