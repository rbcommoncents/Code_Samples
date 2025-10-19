# Controlling a 74HC595 shift register using GPIOZero
# Hardware: Raspberry Pi + 74HC595 IC + 8 LEDs

from gpiozero import DigitalOutputDevice
from time import sleep

# Define GPIO pins connected to the 74HC595
DATA_PIN = 17    # SER (Serial Data Input)
LATCH_PIN = 27   # RCLK (Register Clock)
CLOCK_PIN = 22   # SRCLK (Shift Register Clock)

# Create DigitalOutputDevice objects for each pin
data  = DigitalOutputDevice(DATA_PIN)
latch = DigitalOutputDevice(LATCH_PIN)
clock = DigitalOutputDevice(CLOCK_PIN)

# Helper: send one byte (8 bits) to the shift register
def shift_out(byte_value: int):
    for bit in range(7, -1, -1):  # send MSB → LSB
        bit_val = (byte_value >> bit) & 1
        data.value = bit_val
        clock.on()
        sleep(0.0001)
        clock.off()

# Helper: latch (apply) the shifted bits to the output pins
def latch_output():
    latch.on()
    sleep(0.0001)
    latch.off()

# Demo pattern: binary count from 0–255 on LEDs
try:
    while True:
        for i in range(256):
            shift_out(i)
            latch_output()
            sleep(0.05)
          
except KeyboardInterrupt:
    print("Exiting gracefully...")
    shift_out(0)
    latch_output()
