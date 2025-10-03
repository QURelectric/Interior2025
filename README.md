
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
- Breadboard + jumper wires
- 1x LED (active-low)
- 1x 330Ω resistor
- 1x pushbutton
- 1x 1602 LCD with I2C backpack


Step by Step instructions
----------------------------------------------------------------------
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
   'git clone https://github.com/QURelectric/Interior2025'
   and then enter
   'cd Interior2025'
   to move into the directory that was just made. 

5. Open the Code in Geany  
   ------------------------
   Geany is a simple text editor with python support.  
   To open the code in Geany, type into the terminal:
   'geany workshop1.py &'

   Alternatively, open Geany from the desktop menu  
   and open the `workshop1.py` file manually.

6. Run the Program  
   ----------------
   From Geany:
     - Press F5, or
     - Click "Build" → "Execute"

   Alternatively, from the terminal:
   'python3 workshop1.py'

   What to expect:
     - The LCD shows:
         Hello, world!
         Press button -->
     - The LED turns ON by default.
     - Pressing the button turns the LED OFF.
     - Releasing the button turns it back ON.

WIRING (BCM GPIO Numbers)
----------------------------------------------------------------------

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

----------------------------------------------------------------------  
REQUIRED LIBRARIES
----------------------------------------------------------------------

Most are pre-installed on Raspberry Pi OS:
- `gpiozero`
- `smbus2`
- `signal` and `time` (standard Python)

If needed:
```bash
pip3 install smbus2
