# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class Ishibashi:

    def __init__(self, mode="bcm"):
      if mode is "bcm":
        GPIO.setmode(GPIO.BCM)
      elif mode is "pin":
        GPIO.setmode(GPIO.BOARD)
      else:
        raise Exception("No such PinMode!")

    def should_be_high(self, gpio):
      return 'HIGH'

    def should_be_low(self, gpio):
      return 'LOW'

    def check_volt():
      return 'checking volt'


