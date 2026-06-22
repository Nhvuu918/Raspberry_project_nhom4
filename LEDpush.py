from gpiozero import Button, LED
from signal import pause
button = Button(17)
red = LED(18)
print("ok, nhan nut")
button.when_pressed = red.toggle
pause()
