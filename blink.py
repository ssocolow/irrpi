from gpiozero import LED
from time import sleep

led = LED(26)
t = 2
while True:
    led.on()
    sleep(t)
    led.off()
    sleep(t)
