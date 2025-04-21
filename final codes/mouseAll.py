import time as time
import RPi.GPIO as GPIO
import mouseLib
import random

#Set GIIO pin numbering
GPIO.setmode(GPIO.BCM)

#Right 10cm sensor
GPIO.setup(6, GPIO.IN)

#Left 10cm sensor
GPIO.setup(5, GPIO.IN)

#Right 5cm sensor
GPIO.setup(15, GPIO.IN)

#Left 5cm sensor
GPIO.setup(14, GPIO.IN)

#Front 10cm sensor
GPIO.setup(18, GPIO.IN)

## Print statements 

#print ('Front sensor')
#print (GPIO.input(18))

#print ('Right 5cm sensor')
#print (GPIO.input(15))

#print ('Right 10cm sensor')
#print (GPIO.input(6))

#print ('Left 5cm sensor')
#print (GPIO.input(14))

#print ('Left 10cm sensor')
#print (GPIO.input(5))

#Initial right side pins
GPIO.setup(27, GPIO.OUT) #1EN
GPIO.setup(2, GPIO.OUT) #1A
GPIO.setup(3, GPIO.OUT) #1B

#Initial left side pins
GPIO.setup(22, GPIO.OUT) #2EN
GPIO.setup(4, GPIO.OUT) #2A
GPIO.setup(17, GPIO.OUT) #2B

##5 cm sensor time.sleep
correctSensorTurn= 0.03
correctForward = 0.4

##10 cm sensor time.sleep
turnDirSleepOne = 0.3
turnDirSleepTwo = 0.2

##Direction and Forward time.sleep
turnDirectionSleep = 0.2
turnForwardSleep = 0.1

#Defining a function called obstacle.
def obstacle():
	while(1):
		if (GPIO.input(18) == 1 and GPIO.input(5) == 0 and GPIO.input(6) == 0):
			
			# 5cm sensors ####
			
			#Front open, Right open
			mouseLib.stop()
			mouseLib.forwardStop()
			if (GPIO.input(18) == 1 and GPIO.input(14) == 0 and GPIO.input(15) == 1):
				mouseLib.stop()
				mouseLib.turnRight()
				time.sleep(correctSensorTurn)
				mouseLib.stop()
				mouseLib.forward()
				time.sleep(correctForward)
				mouseLib.stop()
			
			#Front open, Left close	
			elif (GPIO.input(18) == 1 and GPIO.input(15) == 0 and GPIO.input(14) == 1):
				mouseLib.stop()
				mouseLib.turnLeft()
				time.sleep(correctSensorTurn)
				mouseLib.stop()
				mouseLib.forward()
				time.sleep(correctForward)
				mouseLib.stop()
    	
    	# 10cm sensors ####		
		elif (GPIO.input(18) == 0 and GPIO.input(5) == 0 and GPIO.input(6) == 1):
			mouseLib.stop()
			time.sleep(turnDirectionSleep)
			mouseLib.turnRight()
			time.sleep(turnDirectionSleep)
			mouseLib.stop()
			mouseLib.forward()
			time.sleep(turnForwardSleep)
			mouseLib.stop()
		
		elif (GPIO.input(18) == 0 and GPIO.input(5) == 1 and GPIO.input(6) == 0):
			mouseLib.stop()
			time.sleep(turnDirectionSleep)
			mouseLib.turnLeft()
			time.sleep(turnDirectionSleep)
			mouseLib.stop()
			mouseLib.forward()
			time.sleep(turnForwardSleep)
			mouseLib.stop()
		
		#For obstacles on all three sides
		elif (GPIO.input(18) == 0 and GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(14) and GPIO.input(15)):
			mouseLib.stop()
			time.sleep(turnDirectionSleep)
			mouseLib.turnLeft()
			time.sleep(turnDirectionSleep)
			mouseLib.stop()
			mouseLib.forward()
			time.sleep(turnForwardSleep)
			mouseLib.stop()
		
		#For T Junction
		elif (GPIO.input(6) == 1 and GPIO.input(18) == 0 and GPIO.input(5) == 1):
		    ranNum = random.randint(0,1)
		    if (ranNum > 0):
		        time.sleep(turnDirectionSleep)
		        mouseLib.turnRight()
		        time.sleep(turnDirectionSleep)
		        mouseLib.stop()
		        mouseLib.forward()
		        time.sleep(turnForwardSleep)
		        mouseLib.stop()
		        
		    else:
		        time.sleep(turnDirectionSleep)
		        mouseLib.turnLeft()
		        time.sleep(turnDirectionSleep)
		        mouseLib.stop()
		        mouseLib.forward()
		        time.sleep(turnForwardSleep)
		        mouseLib.forward()
		        time.sleep(turnForwardSleep)
		        mouseLib.stop()
		
		#For Forward & Right        
		elif (GPIO.input(6) == 1 and GPIO.input(18) == 1 and GPIO.input(5) == 0):
		    ranNum = random.randint(0,1)
		    if (ranNum > 0):
		        time.sleep(0.1)
		        mouseLib.forward()
		        time.sleep(0.3)
		        mouseLib.stop()
		        
		    else:
		        time.sleep(0.2)
		        mouseLib.turnRight()
		        time.sleep(0.2)
		        mouseLib.stop()
		        mouseLib.forward()
		        time.sleep(0.2)
		        mouseLib.stop()
		           
		#For Forward & Left        
		elif (GPIO.input(6) == 0 and GPIO.input(18) == 1 and GPIO.input(5) == 1):
		    ranNum = random.randint(0,1)
		    if (ranNum > 0):
		        time.sleep(0.2)
		        mouseLib.turnLeft()
		        time.sleep(0.2)
		        mouseLib.stop()
		        mouseLib.forward()
		        time.sleep(0.2)
		        mouseLib.stop()
		    else:
		        time.sleep(0.3)
		        mouseLib.forward()
		        time.sleep(0.3)
		        mouseLib.stop()
		        
		elif (GPIO.input(6) == 1 and GPIO.input(18) == 1 and GPIO.input(5) == 1):
		    ranNum = random.randint(0,2)
		    if (ranNum == 0):
		        time.sleep(turnDirSleepOne)
		        mouseLib.turnLeft()
		        time.sleep(turnDirSleepTwo)
		        mouseLib.stop()
		        mouseLib.forward()
		        time.sleep(turnDirSleepTwo)
		        mouseLib.stop()
		    
		    elif (ranNum == 1):
		    	time.sleep(turnDirSleepOne)
		    	mouseLib.turnRight()
		    	time.sleep(turnDirSleepTwo)
		    	mouseLib.stop()
		    	mouseLib.forward()
		    	time.sleep(turnDirSleepTwo)
		    	mouseLib.stop()
		    	
		    else:
		        time.sleep(turnDirSleepOne)
		        mouseLib.forward()
		        time.sleep(turnDirSleepTwo)
		        mouseLib.stop()
		        
obstacle()  #Runs the obstacle function

     


