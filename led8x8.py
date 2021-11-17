import RPi.GPIO as GPIO
from shifter import Shifter
import multiprocessing
import time




class LED8x8():
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)   
  
    self.pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
    self.row = [0b00000001, 0b00000010, 0b00000100, 0b00001000, 0b00010000, 0b00100000, 0b01000000, 0b10000000]
    self.mask = 0b11111111
    self.p = multiprocessing.Process(name = 'smiley', target = self.display)
    self.p.daemon = True
    self.p.start
    self.smiley = multiprocessing.Array('b', 2)
  

  def display(self):
    for i in range(8):
      self.shifter.shiftByte(~(self.mask & self.pattern[i]))
      self.shifter.shiftByte(self.row[i])
      self.shifter.latch(self.shifter.latchPin)
    time.sleep(0.001)

    