# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example displays the basic animations in sequence, at a five second interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.

This example may not work on SAMD21 (M0) boards.
"""
import board
import neopixel
from adafruit_macropad import MacroPad

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet

from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import (
    PURPLE,
    WHITE,
    AMBER,
    JADE,
    TEAL,
    PINK,
    MAGENTA,
    ORANGE,
)

macropad = MacroPad()

# Update to match the pin connected to your NeoPixels
pixel_pin = board.SDA
# Update to match the number of NeoPixels you have connected
pixel_num = 50

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

solid = Solid(pixels, color=PINK)
blink = Blink(pixels, speed=0.5, color=JADE)
colorcycle = ColorCycle(pixels, speed=0.4, colors=[MAGENTA, ORANGE, TEAL])
chase = Chase(pixels, speed=0.1, color=WHITE, size=3, spacing=6)
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)
rainbow = Rainbow(pixels, speed=0.01)

animation_number = 0

animations = [
    solid,
    blink,
    colorcycle,
    chase,
    comet,
    pulse,
    rainbow,
    ]

animation = comet
prev_encoder = macropad.encoder
speed = 0.1

def create_animation():
    global animation
    number = animation_number
    print("number: ", number)
    if number == 0:
        animation = Solid(pixels, color=PINK)
        print("solid")
    if number == 1:
        animation = Blink(pixels, speed=speed, color=JADE)
        print("blink")
    if number == 2:
        animation = ColorCycle(pixels, speed=speed, colors=[MAGENTA, ORANGE, TEAL])
        print("colour cycle")
    if number == 3:
        animation = Chase(pixels, speed=speed, color=WHITE, size=3, spacing=6)
        print("chase")
    if number == 4:
        animation = Comet(pixels, speed=speed, color=PURPLE, tail_length=10, bounce=True)
        print("comet")
    if number == 5:
        animation = Pulse(pixels, speed=speed, color=AMBER, period=3)
        print("pulse")
    if number == 6:
        animation = Rainbow(pixels, speed=speed)
        print("rainbow")
    if number == 7:
        animation = Sparkle(pixels, speed=speed, color=PINK)
        print("sparkle")
    if number == 8:
        animation = RainbowSparkle(pixels, speed=speed)
        print("rainbow sparkle")
    if number == 9:
        animation = RainbowComet(pixels, speed=speed)
        print("rainbow comet")
    if number == 10:
        animation = SparklePulse(pixels, speed=0.1, color=TEAL, period=speed)
        print("sparkle pulse")

    print("speed: ", speed)


while True:
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        animation_number = key_event.key_number
        create_animation()
    if macropad.encoder != prev_encoder:
        speed = (macropad.encoder / 100) + 0.1
        prev_encoder = macropad.encoder
        create_animation()
    animation.animate()
