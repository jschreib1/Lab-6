import RPi.GPIO as GPIO
from shifter import Shifter
import time

global pattern
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

class LED8x8():
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)   

  def display(self):
    for i in range(8):
      self.shifter.shiftByte(pattern[i])
      self.shifter.shiftByte(1 << i)
    self.shifter.ping(self.shifter.latchPin)