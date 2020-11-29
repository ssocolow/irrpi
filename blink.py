from gpiozero import LED
from time import sleep

led = LED(26)
t = 0.5
for i in range(10):
    print("yol0")
    led.on()
    sleep(t)
    led.off()
    sleep(t)
