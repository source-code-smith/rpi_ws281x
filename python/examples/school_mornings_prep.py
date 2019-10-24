#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Herman Smith (herman@sourcecodesmith.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from datetime import timedelta
from neopixel import *
import argparse

# def Color(red, green, blue, white = 0):
# 	"""Convert the provided red, green, blue color to a 24-bit color value.
# 	Each color component should be a value 0-255 where 0 is the lowest intensity
# 	and 255 is the highest intensity.
# 	"""
# 	return (white << 24) | (red << 16)| (green << 8) | blue

# Morning stages configuration
BLUE = Color(0, 0, 255)
ORANGE = Color(50, 255, 0)
GREEN = Color(255, 0, 0)
RED = Color(0, 255, 0)

INTERVAL_DURATION_SECONDS = 1

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class Morning_Prep_Stage(object):
    def __init__(self, title, color, colorSymbol, commencement, duration):
        self.title = title
        self.color = color
        self.colorSymbol = colorSymbol
        self.commencement = commencement
        self.duration = duration

class Strip_Mock(object):
    def __init__(self, length):
        self.STRIP = []
        for i in range(length):
            self.STRIP.append(0)

    def setPixelColor(self, i, color):
        self.STRIP[i] = color

    def show(self):
        print(self.STRIP)

def calculateStagesDuration(stages):
    result = 0
    for stage in stages:
        result += stage.duration
    return result

def initializeStages(strip, stages):    
    for stage in stages:
        for i in range(stage.commencement, stage.commencement+stage.duration):
            strip.setPixelColor(i, stage.color)
            # strip.setPixelColor(i, stage.colorSymbol)
    strip.show()

def updateProgressForStages(strip, stages, elapsed_seconds):
    for stage in stages:
        if elapsed_seconds/INTERVAL_DURATION_SECONDS >= stage.commencement:
            for i in range(stage.commencement, int(elapsed_seconds/INTERVAL_DURATION_SECONDS)):
                strip.setPixelColor(i, RED)
                # strip.setPixelColor(i, 'R')
            strip.show()

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    # OR

    # # Mock Strip
    # strip = Strip_Mock(LED_COUNT)

    print ('Press Ctrl-C to quit.')

    stages = []
    stages.append(Morning_Prep_Stage('Wake', BLUE, 'B', 0, 15))
    stages.append(Morning_Prep_Stage('Eat and Dress', ORANGE, 'O', 15, 30))
    stages.append(Morning_Prep_Stage('Bathroom', GREEN, 'G', 45, 15))

    initializeStages(strip, stages)

    stages_duration = timedelta(seconds = calculateStagesDuration(stages)*INTERVAL_DURATION_SECONDS)
    start_time = timedelta(seconds = time.time())

    time.sleep(INTERVAL_DURATION_SECONDS)
    now_time = timedelta(seconds = time.time())
    lapsed_time = now_time - start_time

    try:
        while lapsed_time <= stages_duration:
    	    #print('*')

            now_time = timedelta(seconds = time.time())
            lapsed_time = now_time - start_time
            updateProgressForStages(strip, stages, lapsed_time.total_seconds())

            time.sleep(INTERVAL_DURATION_SECONDS)

        while True:
            theaterChase(strip, RED)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
