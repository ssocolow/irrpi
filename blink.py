from gpiozero import LED
from time import sleep

led = LED(26)
t = 1
for i in range(10):
    print("yol")
    led.on()
    sleep(t)
    led.off()
    sleep(t)
