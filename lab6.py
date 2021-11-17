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
'''
def move(row, column):
  move += random.randint(-1,1)
  while space < 1 or space > 8:
    space += random.randint(-1,1)
'''
global row, column
#row = random.randint(0,7) #initial row for random walk
#myLED.smiley[0] = myLED.pattern[row]
#column = random.randint(0,7) #initial column for random walk
#myLED.smiley[1] = myLED.pattern[column]
x = random.randint(0,7)
y = random.randint(0,7)
myLED.smiley[0] = myLED.pattern[x]
myLED.smiley[1] = myLED.pattern[y]

try:
  while True:
    movex = random.randint(-1,1)
    x+=movex
    movey = random.randint(-1,1)
    y+=movey
    myLED.smiley[0] = myLED.pattern[x]
    if x < 0: x = 0
    if x > 7: x = 7
    myLED.smiley[1] = myLED.pattern[y]
    if y < 0: y = 0
    if y > 7: y = 7
    myLED.shifter.shiftByte((1 << (myLED.smiley[0]-1)))
    myLED.shifter.shiftByte((1 << (myLED.smiley[1]-1)))
    #myLED.display() commented out for the random walk
    #time.sleep(0.001)
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
