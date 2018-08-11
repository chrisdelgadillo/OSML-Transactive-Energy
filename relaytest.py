import RPi.GPIO as IO
import time
#Define relay pin for signal
signalPin=4

def relay():
	if power <= 500:
		IO.output(signalPin,IO.LOW)
	else:
		IO.output(signalPin,IO.HIGH)
def setup():
	IO.setmode(IO.BCM)
	IO.setwarnings(False)
	IO.setup(signalPin, IO.OUT)

setup()
while 1:
	print('How much power(watts) is sys 1 consuming?')
	power = input()
	relay()
	print('Power transaction successful.')
	time.sleep(3)

