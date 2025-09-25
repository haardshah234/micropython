import machine
from time import sleep

potPin = 26
myPot = machine.ADC(potPin)
while True:
    potVal = myPot.read_u16()
    print(f'{potVal*(3.3/65535):.2f}V')
    sleep(.5)