from gpiozero import RGBLED
from time import sleep
led = RGBLED(red=17, green=27, blue=22)
led.red = 1  
print('紅燈亮')
sleep(0.5)
led.color = (0, 0, 0)  
sleep(0.5)

led.blue = 1
print('藍燈亮')
sleep(0.5)
led.color = (0, 0, 0)  
sleep(0.5)

led.green = 1
print('綠燈亮')
sleep(0.5)
led.color = (0, 0, 0)  
sleep(0.5)

led.green = 0.5
print('半綠燈亮')
sleep(0.5)
led.color = (0, 0, 0)  
sleep(0.5)

led.color = (1, 1, 0)
print('黃色')
sleep(0.5)
led.color = (0, 0, 0)  
