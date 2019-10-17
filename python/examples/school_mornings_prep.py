#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from datetime import timedelta
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

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class Morning_Prep_Stage:
  def __init__(self, color, duration):
    self.color = color
    self.duration = duration

def updateProgressForStages(stages, elapsed_seconds):
    print(elapsed_seconds)
    for item in stages.items():
        print(item)

# # Define functions which animate LEDs in various ways.
# def colorWipe(strip, color, wait_ms=50):
#     """Wipe color across display a pixel at a time."""
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, color)
#         strip.show()
#         time.sleep(wait_ms/1000.0)

# def theaterChase(strip, color, wait_ms=50, iterations=10):
#     """Movie theater light style chaser animation."""
#     for j in range(iterations):
#         for q in range(3):
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, color)
#             strip.show()
#             time.sleep(wait_ms/1000.0)
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, 0)

# def wheel(pos):
#     """Generate rainbow colors across 0-255 positions."""
#     if pos < 85:
#         return Color(pos * 3, 255 - pos * 3, 0)
#     elif pos < 170:
#         pos -= 85
#         return Color(255 - pos * 3, 0, pos * 3)
#     else:
#         pos -= 170
#         return Color(0, pos * 3, 255 - pos * 3)

# def rainbow(strip, wait_ms=20, iterations=1):
#     """Draw rainbow that fades across all pixels at once."""
#     for j in range(256*iterations):
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, wheel((i+j) & 255))
#         strip.show()
#         time.sleep(wait_ms/1000.0)

# def rainbowCycle(strip, wait_ms=20, iterations=5):
#     """Draw rainbow that uniformly distributes itself across all pixels."""
#     for j in range(256*iterations):
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
#         strip.show()
#         time.sleep(wait_ms/1000.0)

# def theaterChaseRainbow(strip, wait_ms=50):
#     """Rainbow movie theater light style chaser animation."""
#     for j in range(256):
#         for q in range(3):
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, wheel((i+j) % 255))
#             strip.show()
#             time.sleep(wait_ms/1000.0)
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # # Create NeoPixel object with appropriate configuration.
    # strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # # Intialize the library (must be called once before other functions).
    # strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        wakeUp = Morning_Prep_Stage(BLUE, 15)
        eatAndDress = Morning_Prep_Stage(ORANGE, 30)
        wipeFaceBrushTeeth = Morning_Prep_Stage(GREEN, 15)
        # gotoCar

        stages = dict(
            wakeUp = Morning_Prep_Stage(BLUE, 15),
            eatAndDress = Morning_Prep_Stage(ORANGE, 30),
            wipeFaceBrushTeeth = Morning_Prep_Stage(GREEN, 15)
        )
        
        start_time = timedelta(seconds = time.time())
        while True:
            time.sleep(1)
            now_time = timedelta(seconds = time.time())
            lapsed_time = now_time - start_time
            updateProgressForStages(stages, lapsed_time.total_seconds())
        #     print ('Color wipe animations.')
        #     colorWipe(strip, Color(255, 0, 0))  # Red wipe
        #     colorWipe(strip, Color(0, 255, 0))  # Blue wipe
        #     colorWipe(strip, Color(0, 0, 255))  # Green wipe
        #     print ('Theater chase animations.')
        #     theaterChase(strip, Color(127, 127, 127))  # White theater chase
        #     theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        #     theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
        #     print ('Rainbow animations.')
        #     rainbow(strip)
        #     rainbowCycle(strip)
        #     theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
