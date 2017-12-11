
def piezo():
    pin = 15
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)    #motor dir2 pin
    my_pwm = GPIO.PWM(pin, 500)	#creates pwm object
    while(1):
        my_pwm.start(100)

if __name__== "__main__" :
    import RPi.GPIO as GPIO
    try:
            piezo()
    except KeyboardInterrupt:
            pass
    finally:
            GPIO.cleanup()
