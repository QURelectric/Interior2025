######## Interior Workshop 1: Basics of IO with Raspberry Pi ##########

# gpiozero is the library that allows the python code to interact with the physical pins on the pi
# see https://gpiozero.readthedocs.io/en/
from gpiozero import LED, Button
# The signal and time libraries lets us use time to control the execution of our program
from signal import pause
import time
# SMBus is a library that gives us extra tools to use the I2C interface (needed for the 16x2 display)
from smbus2 import SMBus

# ========== SECTION 1: LED and Button ==========
#LED and Button are built in classes in gpiozero. 
#See docs section 15.1.1 (led) and 14.1.1 (button)

# Active-low LED on GPIO17 (set active_high=False to invert logic)
led = LED(17, active_high=False)

# Active-low Button on GPIO27 with internal pull-up
button = Button(27, pull_up=True)

# Turn the LED ON initially
led.on()

# Turn LED off when button is pressed, on when released
button.when_pressed = led.off()
button.when_released = led.on()

# ========== SECTION 2: I2C LCD Display ==========
# The common 1602 display usually uses up to 8 pins to transmit data, but many modules are equipped
# with an additional board that converts the signal to a simpler I2C interface, which only needs 4 pins. 
# I2C is a signaling standard that many sensors and other devices use to comminicate back and forth with a host device. 
# The section will require us to set up our own functions to send the correct information along the bus.

# LCD I2C address (commonly 0x27 or 0x3F)
# Every I2C device has an address that is usually hard-coded into the component. 
I2C_ADDR = 0x27

# LCD control constants
LCD_WIDTH = 16
LCD_CHR = 1
LCD_CMD = 0
LCD_LINE_1 = 0x80 
LCD_LINE_2 = 0xC0
LCD_BACKLIGHT = 0x08
ENABLE = 0b00000100

#this line tells the pi to use I2C bus 1, which uses GPIO pins 2 and 3. 
bus = SMBus(1)  # Use I2C bus 1

# the following are helper functions that help us send the correct sequence of bits to the lcd display.
# usually, they would be hidden behind a library. it is not important to understand the specifics of the at this time. 
def lcd_byte(bits, mode):
    high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT
    bus.write_byte(I2C_ADDR, high)
    toggle_enable(high)
    bus.write_byte(I2C_ADDR, low)
    toggle_enable(low)

def toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, bits | ENABLE)
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, bits & ~ENABLE)
    time.sleep(0.0005)

def lcd_init():
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(0.005)

def lcd_message(text, line):
    text = text.ljust(LCD_WIDTH)
    lcd_byte(line, LCD_CMD)
    for char in text:
        lcd_byte(ord(char), LCD_CHR)

# Finally, we can initialize the display and write a message
lcd_init()
lcd_message("Hello, world!", LCD_LINE_1)
lcd_message("Press button -->", LCD_LINE_2)

print("System ready. Press the button to control the LED.")
# This line keeps the program from ending early. 
pause()
