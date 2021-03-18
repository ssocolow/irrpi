
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

def blue():
    GPIO.output(26, False)
    GPIO.output(13, True)
    GPIO.output(19, True)
def red():
    GPIO.output(26, True)
    GPIO.output(13, False)
    GPIO.output(19, True)
def green():
    GPIO.output(26, True)
    GPIO.output(13, True)
    GPIO.output(19, False)
red()

