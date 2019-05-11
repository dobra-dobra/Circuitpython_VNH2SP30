# Circuitpython library for SparkFun Monster Moto Shield
Circuitpython port of Arduino library for SparkFun Monster Moto Shield
This shield is designed for 5V devices, but it was tested with Adafruit Grand Central and it does work well. Except...

## Warning
Pins A2 and A3 are used for current sensing. Dependig on current drawn by motors this may go above 3.3 V and damage your board. You may want to disable this feature by desoldering resistors R5 and R14 from the shield or by cutting header leads for pins A2 and A3.

Linkt to the shield: https://www.sparkfun.com/products/10182

## Usage example
### Import library:

from vnh2sp30 import *

### Run motor 0 clockwise at 50% PWM:

motorGo(0, CW, 32767)

### Run motor 1 counter clockwise at 100% PWM:

motorGo(1, CCW, 65535)

### Brake motor 0 to VCC (block motor):

motorGo(0, BRAKEVCC)

### Brake motor 1 to GND (without blocking):

motorGo(1, BRAKEGND)

### Turn off motor 0:

motorOff(0)
