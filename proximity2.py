import time
import RPi.GPIO as GPIO


class psensor:
    
	def __init__(self, name, pins):
		self.name = name
		self.pins = pins
		self.trigger = self.pins[0]#define 1st pin that determines direction
		self.echo = self.pins[1]	#define 2nd pin that determines direction
		self.wasON = False
		self.triggered = False
    
		
	def pinSetup(self):
                #GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.trigger, GPIO.OUT)    #motor dir1 pin
		GPIO.setup(self.echo, GPIO.IN)
		GPIO.output(self.trigger, False)
		time.sleep(0.1)
		
		
		
	def measure(self):
			if (!self.triggered)
				GPIO.output(self.trigger, True)
				time.sleep(0.00001)
				GPIO.output(self.trigger, False)
				self.triggered = True
					             
            if GPIO.input(self.echo)==0:
				if self.wasON:
					self.wasON = False
					self.start = time.time()
					elapsed = self.start - self.stop
					distance = elapsed*34300/2
					self.triggered = False
					return distance
				self.wasON = False

            if GPIO.input(self.echo)==1:
                if !self.wasON:
					self.wasON = True
					self.stop = time.time()
		
	def measure_average(self):
		distance1=self.measure()
		distance2=self.measure()
		distance3=self.measure()
		distance = distance1 + distance2 + distance3
		distance = distance / 3
		return distance
