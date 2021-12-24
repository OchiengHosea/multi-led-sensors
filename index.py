import RPi.GPIO as GPIO
import time
from sys import argv

pins = dict(
    LEDa=17,
    LEDb=18,
    LEDc=22,
    LEDd=23
    )

whichled=argv[1]
ledaction = argv[2]

GPIO.setmode(GPIO.BCM)
for k, v in pins:
    GPIO.setup(k, GPIO.OUT)

if ledaction == "on":
    if whichled == "all":
        for k, v in pins:
            GPIO.output(k, True)
    else:
        for k, v in pins:
            if k.endswith(whichled):
                GPIO.output(k, True)
