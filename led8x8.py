import RPi.GPIO as GPIO
from shifter import Shifter
import time

global pattern
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

row = [0b00000001, 0b00000010, 0b00000100, 0b00001000, 0b00010000, 0b00100000, 0b01000000, 0b10000000]
class LED8x8():
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)   

  def display(self):
    for i in range(8):
      self.shifter.shiftByte(pattern[i])
      self.shifter.shiftByte(row[i])
    self.shifter.ping(self.shifter.latchPin)
    time.sleep(0.001)