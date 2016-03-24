# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class Ishibashi:

    def __init__(self, mode="bcm"):
      self.GPIO = GPIO
      if mode is "bcm":
        self.GPIO.setmode(self.GPIO.BCM)
      elif mode is "pin":
        self.GPIO.setmode(self.GPIO.BOARD)
      else:
        raise Exception("No such PinMode!")

    def should_be_high(self, gpio):
      self.GPIO.setup(gpio,self.GPIO.IN)
      if GPIO.input(gpio):
        return True
      else:
        return False

    def should_be_low(self, gpio):
      self.GPIO.setup(gpio,self.GPIO.IN)
      if not GPIO.input(gpio):
        return True
      else:
        return False

    def all_should_be_low(self, *args):
      for gpio in args:
        if not self.should_be_low(gpio):
          return False
      return True

    def all_should_be_high(self, *args):
      for gpio in args:
        if not self.should_be_high(gpio):
          return False
      return True

    def in_time(self, wait_time, method):
      result = method
      wait_time = wait_time / 1000.0
      time.sleep(wait_time)
      return result


    def finish(self):
      self.GPIO.cleanup()


