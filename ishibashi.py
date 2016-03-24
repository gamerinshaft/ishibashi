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

    def check_volt():
      return 'checking volt'

    # テスト対象のメソッド
    def return_hoge(self):
        return 'hoge'

    # テスト対象のメソッド
    def return_poyo(self):
        return 'poyo'

    def finish():
      self.GPIO.cleanup()
