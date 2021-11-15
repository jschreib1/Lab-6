import RPi.GPIO as GPIO
from shifter import Shifter
import multiprocessing
import time


global pattern
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

global row
row = [0b00000001, 0b00000010, 0b00000100, 0b00001000, 0b00010000, 0b00100000, 0b01000000, 0b10000000]
mask = 0b11111111

global smiley
smiley = multiprocessing.Array('b', 2)

class LED8x8():
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)   

  def display(self):
    for i in range(8):
      self.shifter.shiftByte(~(mask & pattern[i]))
      self.shifter.shiftByte(row[i])
      self.shifter.latch(self.shifter.latchPin)
    time.sleep(0.001)

  def multismiley(self):
    for i in range(8):
      smiley[0], smiley[1] = pattern[i], row[i]
    self.shifter.shiftByte(~(mask & smiley[0]))
    self.shifter.shiftByte(smiley[1])
    time.sleep(0.001)
    