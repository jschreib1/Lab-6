import RPi.GPIO as GPIO
from shifter import Shifter
import time
from led8x8 import LED8x8

data, latch, clock = 23, 24, 25
myLED = LED8x8(data, latch, clock)
while True:
  myLED.display()
  time.sleep(0.001)