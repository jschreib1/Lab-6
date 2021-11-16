import multiprocessing
import RPi.GPIO as GPIO
from shifter import Shifter
import time
from led8x8 import LED8x8
import random

data, latch, clock = 23, 24, 25
myLED = LED8x8(data, latch, clock)
myShifter = Shifter(data, latch, clock)
random.seed()

def move(space):
  space += random.randint(-1,1)
  while space < 1 or space > 8:
    space += random.randint(-1,1)

global row, column
row = random.randint(1,8) #initial row for random walk
column = random.randint(1,8) #initial column for random walk

try:
  while True:
    myLED.smiley[0] = move(row)
    myLED.smiley[1] = move(column)
    #myLED.display() commented out for the random walk
    #time.sleep(0.001)
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
