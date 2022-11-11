import sys
import datetime
import time
import RPi.GPIO as GPIO
import tm1637
import random

Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightness(1)
while (True):
    currenttime = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
    Display.Show(currenttime)
    time.sleep(2)