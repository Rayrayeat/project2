from gpiozero import LEDBoard
from gpiozero import Button, LED
from signal import pause
from time import sleep
   
def Action():
    leds.Red.on()
    sleep(1)
    leds.Red.off()
    leds.Green.on()
    sleep(1)
    leds.Green.off()
    leds.Blue.on()
    sleep(1)
    leds.Blue.off()

leds = LEDBoard(Red=17, Green=27, Blue=22)
button = Button(18, hold_time=2)

button.when_held = Action
pause()
