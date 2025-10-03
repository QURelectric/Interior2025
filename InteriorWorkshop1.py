# =====================================
# Raspberry Pi Workshop: Basic I/O with gpiozero and I2C LCD
# =====================================
# Hardware:
# - 1x Active-low LED on GPIO17
# - 1x Active-low Pushbutton on GPIO27
# - 1x 1602 I2C LCD (commonly using I2C address 0x27)
# =====================================

from gpiozero import LED, Button
from signal import pause
import time
from smbus2 import SMBus

# =====================================
# SECTION 1: OUTPUT — Controlling an Active-Low LED
# =====================================

print("=== LED Output Demo ===")

# Active-low LED: we invert the logic manually
led = LED(17, active_high=False)  # GPIO17, active_low = True

print("Blinking the LED 5 times...")

for i in range(5):
    led.on()    # Actually sets GPIO LOW (active low)
    time.sleep(0.5)
    led.off()   # Sets GPIO HIGH
    time.sleep(0.5)

print("Done blinking.\n")

# =====================================
# SECTION 2: INPUT — Reading an Active-Low Button
# =====================================

print("=== Button Input Demo ===")

# Button connected to GPIO27, using internal pull-up
button = Button(27, pull_up=True)  # Active-low button

# Link button directly to LED (mirrors state)
print("Press the button to turn ON the LED. Release to turn it OFF.")
print("Press Ctrl+C to move on to the LCD section.\n")

# Automatically turns LED on when button is pressed
button.when_pressed = led.on
button.when_released = led.off

try:
    pause()  # Wait forever until Ctrl+C
except KeyboardInterrupt:
    print("\nMoving to the LCD demo...")

# =====================================
# SECTION 3: OUTPUT — Displaying Text on a 1602 I2C LCD
# =====================================

# Based on PCF8574 I2C backpack
# Common I2C address: 0x27 or 0x3F
# You can confirm with: sudo i2cdetect -y 1

I2C_ADDR = 0x27  # Adjust if needed
LCD_WIDTH = 16

# LCD Commands
LCD_CHR = 1  # Data
LCD_CMD = 0  # Command

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

LCD_BACKLIGHT = 0x08  # On
ENABLE = 0b00000100   # Enable bit

bus = SMBus(1)  # I2C bus 1 on Pi

def lcd_byte(bits, mode):
    """Send byte to LCD in 4-bit mode"""
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(0.0005)

def lcd_init():
    """Initialize LCD display"""
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(0.005)

def lcd_message(message, line):
    """Send message to LCD"""
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for char in message:
        lcd_byte(ord(char), LCD_CHR)

print("=== LCD Display Demo ===")
lcd_init()
lcd_message("Hello, world!", LCD_LINE_1)
lcd_message("Raspberry Pi <3", LCD_LINE_2)

print("Message displayed on LCD.")

# =====================================
# CLEANUP
# =====================================

# Turn off the LED for good measure
led.off()
print("Workshop complete. You can now extend this code!")

