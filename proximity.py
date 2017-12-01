import time


class psensor:
    
	def __init__(self, name, trigger, echo):
		self.name = name
		self.pins = pins
		self.trigger = trigger	#define 1st pin that determines direction
		self.echo = echo	#define 2nd pin that determines direction
		
	def pinSetup(self):		
		GPIO.setup(self.trigger, GPIO.OUT)    #motor dir1 pin
		GPIO.setup(self.echo, GPIO.OUT)    #motor dir2 pin	
		
	def measure(self):
		# This function measures a distance
		GPIO.output(self.trigger, True)
		time.sleep(0.00001)
		GPIO.output(self.trigger, False)
		start = time.time()

		while GPIO.input(self.echo)==0:
			start = time.time()

		while GPIO.input(self.echo)==1:
			stop = time.time()

		elapsed = stop-start
		distance = (elapsed * 34300)/2

		return distance
		
	def measure_average():
		# This function takes 3 measurements and
		# returns the average.
		distance1=self.measure()
		time.sleep(0.1)
		distance2=self.measure()
		time.sleep(0.1)
		distance3=self.measure()
		distance = distance1 + distance2 + distance3
		distance = distance / 3
		return distance