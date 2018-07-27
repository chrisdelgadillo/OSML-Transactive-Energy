 
import RPi.GPIO as IO
import time

#Define GPIO Pins for (CS, CLK, MISO & MOSI)
SPICLK  = 2
SPIMISO = 3
SPIMOSI = 4
SPICS   = 17

#Set SPI pins as Input/Outout
def setup():
	IO.setmode(IO.BCM)
	IO.setwarnings(False)
	IO.setup(SPICLK,IO.OUT)
	IO.setup(SPIMISO, IO.IN)
	IO.setup(SPIMOSI,IO.OUT)
	IO.setup(SPICS,IO.OUT, initial = IO.HIGH)


def read(channel):
	#Determine if allowed channel from A0:A7
	if channel > 7 | channel < 0:
		print("error")
		return -1


	#Initialize communication when CS is low
	IO.output(SPICLK,IO.LOW)
	IO.output(SPICS,IO.LOW)

	control  = channel
	if channel == 0:
		control |=0b00011000
	elif channel == 1:
		control |=0b00011001
	elif channel == 2:
		control |=0b00011010
	elif channel == 3:
		control |=0b00011011
	elif channel == 4:
		control |=0b00011100
	elif channel == 5:
		control |=0b00011101
	elif channel == 6:
		control |=0b00011110
	elif channel == 7:
		control |=0b00011111
	for i in range(5):
		if control & 0x10:
			IO.output(SPIMOSI, IO.HIGH)
		else:
			IO.output(SPIMOSI, IO.LOW)
		control <<= 1
		IO.output(SPICLK,IO.HIGH)
		IO.output(SPICLK,IO.LOW)

	char = 0
	for i in range(11):
		IO.output(SPICLK,IO.HIGH)
		IO.output(SPICLK,IO.LOW)
		char <<=1
		if IO.input(SPIMISO):
			char |= 0x1

	IO.output(SPICS,IO.HIGH)
	return char

def mapVoltage(initValue, charMin, charMax, voltMin, voltMax)
    voltTotal = voltMax - voltMin
    charPoint = voltTotal/(charMax - charMin)

    return initValue * charPoint    

def roundValue(value):
	print("{:0.2f}").format(value)


setup() 

while 1:
	time.sleep(0.1)

