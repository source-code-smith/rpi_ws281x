#!/usr/bin/env python3

import time
# from neopixel import *
import argparse

def Color(red, green, blue, white = 0):
	"""Convert the provided red, green, blue color to a 24-bit color value.
	Each color component should be a value 0-255 where 0 is the lowest intensity
	and 255 is the highest intensity.
	"""
	return (white << 24) | (red << 16)| (green << 8) | blue

# Morning stages configuration
BLUE = Color(0, 0, 255)
ORANGE = Color(255, 165, 0)
GREEN = Color(0, 255, 0)

class Morning_Prep_Stage:
  def __init__(self, color, duration):
    self.color = color
    self.duration = duration    

# Main program logic follows:
if __name__ == '__main__':
    stages = dict(
        wakeUp = Morning_Prep_Stage(BLUE, 15),
        eatAndDress = Morning_Prep_Stage(ORANGE, 30),
        wipeFaceBrushTeeth = Morning_Prep_Stage(GREEN, 15)
    )

    for key in stages:
        print(key)

    for item in stages.items():
        print(item)
