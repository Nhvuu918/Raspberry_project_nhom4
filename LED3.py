from gpiozero import LED
from time import sleep

red = LED(18)
green = LED(23)
amber = LED(24)
red.on()
green.off()
amber.off()
while True:
	sleep(2)
	red.off()
	green.on()
	sleep(2)
	green.off()
	amber.on()
	sleep(2)
	red.on()
	amber.off()
	
