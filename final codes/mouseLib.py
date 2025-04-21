import time as time
import RPi.GPIO as GPIO

#Stop
def stop():
	GPIO.output(27,0)
	GPIO.output(2,0)
	GPIO.output(3,0)
	GPIO.output(22,0)
	GPIO.output(4,0)
	GPIO.output(17,0)
	
#Move Forward
def forward():
	GPIO.output(27,1)
	GPIO.output(2,1)
	GPIO.output(3,0)
	GPIO.output(22,1)
	GPIO.output(4,0)
	GPIO.output(17,1)
	
#Move Forward, then Stop
def forwardStop():
	GPIO.output(27,1)
	GPIO.output(2,1)
	GPIO.output(3,0)
	GPIO.output(22,1)
	GPIO.output(4,0)
	GPIO.output(17,1)
	
#Reverse
def reverse():	
	GPIO.output(27,1)
	GPIO.output(2,0)
	GPIO.output(3,1)
	GPIO.output(22,1)
	GPIO.output(4,1)
	GPIO.output(17,0)
	
#Move Right
def turnRight():
	GPIO.output(27,1)
	GPIO.output(2,1)
	GPIO.output(3,0)
	GPIO.output(22,1)
	GPIO.output(4,1)
	GPIO.output(17,0)

#Move Left
def turnLeft():
	GPIO.output(27,1)
	GPIO.output(2,0)
	GPIO.output(3,1)
	GPIO.output(22,1)
	GPIO.output(4,0)
	GPIO.output(17,1)
