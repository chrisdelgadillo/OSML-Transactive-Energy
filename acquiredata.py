# Acquires data from MCP3008

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


CLK = 2
MISO = 3
MOSI = 4
CS = 17

mcp = Adafruit_MCP3008.MCP3008(clk=CLK,cs=CS,miso=MISO,mosi=MOSI)

print("Reading values from MCP3008, press Ctrl-C to quit dude...")
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)

while True:
    
    values = [0]*8
    for i in range(8):

        values[i] = mcp.read_adc(i)
        values[i] = 0
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)