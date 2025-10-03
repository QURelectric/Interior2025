
Interior Workshop 1: Basics of I/O with Raspberry Pi
----------------------------------------------------------------------  
Hardware: Raspberry Pi 4, Breadboard, LED, Button, 1602 I2C LCD  

Language: Python 3 (using gpiozero and smbus2)

 
WORKSHOP OVERVIEW
----------------------------------------------------------------------

This exercise introduces basic hardware I/O using Python on a Raspberry Pi.

You will:
- Control an LED (output)
- Read a pushbutton (input)
- Display text on a 1602 LCD over I2C

  
REQUIRED HARDWARE
----------------------------------------------------------------------

- Raspberry Pi 4
- Raspberry Pi power supply
- USB keyboard
- Monitor or Display
- Breadboard + jumper wires
- 1x LED
- 1x 330Ω resistor
- 1x pushbutton
- 1x 1602 LCD with I2C backpack (Small black pcb attached to the green display pcb)


Step by Step instructions
----------------------------------------------------------------------
0. Set up the Pi
   ---------------
   Plug in the power supply, keyboard, and display to the raspberry pi. The pi should power up and bring you to a home screen.
1. Review the Wiring  
   ------------------
   Follow the wiring guide below.  
   Make sure you are using **BCM GPIO numbers**, not physical pin numbers.  
   For a full Raspberry Pi pinout reference, visit:  
   https://pinout.xyz

2. Understand the Code  
   ---------------------
   This script uses the `gpiozero` library to interact with GPIO pins (LED, Button),  
   and `smbus2` to communicate with the I2C LCD display.  
   For documentation and examples, see:  
   https://gpiozero.readthedocs.io/en/stable/

3. Clone the Repository  
   ---------------------
   On your Raspberry Pi, open a terminal and run:
   ```git clone https://github.com/QURelectric/Interior2025```
   and then enter
   ```cd Interior2025```
   to move into the directory that was just made. 

4. Open the Code in Geany  
   ------------------------
   Geany is a simple text editor with python support.  
   To open the code in Geany, type into the terminal:
   `geany workshop1.py &`

   Alternatively, open Geany from the desktop menu  
   and open the `workshop1.py` file manually.

5. Run the Program  
   ----------------
   From Geany:
     - Press F5, or
     - Click the paper airplane icon

   Alternatively, from the terminal:
   'python3 workshop1.py'

   What to expect:
     - The LCD shows:
         Hello, world!
         Press button -->
     - The LED turns ON by default.
     - Pressing the button turns the LED OFF.
     - Releasing the button turns it back ON.
     - The LED may be dim, and you may also need to adjust the contrast of the LCD. This is done by slowly turning the small white screw on the back of the board.  

WIRING (BCM GPIO Numbers)
----------------------------------------------------------------------
NOTE: The breadboard power rails are color coded, but the color is not always correct.
Always refer to the +/- symbols on the adapter board, where - refers to the ground side.

- LED:
  - GPIO17 → Resistor → LED cathode (short leg)
  - LED anode (long leg) → 3.3V

- Button:
  - GPIO27 → one side of button
  - Other side → GND

- I2C LCD:
  - SDA → GPIO2
  - SCL → GPIO3
  - VCC → 5V
  - GND → GND

REQUIRED LIBRARIES
----------------------------------------------------------------------

Most are pre-installed on Raspberry Pi OS:
- `gpiozero`
- `smbus2`
- `signal` and `time` (standard Python)

Unlikely, but if needed:
```bash
pip3 install smbus2
```
If weird errors occur, check the Raspberry Pi Preferences in settings and tick 'I2C' to be enabled. 

Future Considerations
----------------------------------------------------------------------
- Implementing sensors as inputs
- Using the OLED display
- Wrapping the LCD helper functions in a class
