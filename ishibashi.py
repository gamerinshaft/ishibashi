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
      if self.GPIO.input(gpio):
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

    def detect_high_edge(self, gpio, wait_time):
      self.GPIO.setup(gpio,self.GPIO.IN)
      self.GPIO.add_event_detect(gpio, GPIO.RISING)
      time.sleep(wait_time / 1000.0)
      if self.GPIO.event_detected(gpio):
        return True
      else:
        return False

    def detect_low_edge(self, gpio, wait_time):
      self.GPIO.setup(gpio,self.GPIO.IN)
      self.GPIO.add_event_detect(gpio, GPIO.FALLING)
      time.sleep(wait_time / 1000.0)
      if self.GPIO.event_detected(gpio):
        return True
      else:
        return False

    def detect_high_or_low_edge(self, gpio, wait_time):
      self.GPIO.setup(gpio,self.GPIO.IN)
      self.GPIO.add_event_detect(gpio, GPIO.BOTH)
      time.sleep(wait_time / 1000.0)
      if self.GPIO.event_detected(gpio):
        return True
      else:
        return False

    def finish(self):
      self.GPIO.cleanup()


