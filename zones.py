from machine import Pin, ADC
import time

potPin = 26
myPot = machine.ADC(potPin)

greenPin = 12
yellowPin = 13
redPin = 14

greenLed = Pin(greenPin,Pin.OUT)
yellowLed = Pin(yellowPin,Pin.OUT)
redLed = Pin(redPin,Pin.OUT)

while True:
    val = (myPot.read_u16() * 3.3/65535)
    val = val*100/3.3
    print(f'{(val):.2f}%')
    if val > (90):
        greenLed.value(0)
        yellowLed.value(0)
        redLed.value(1)
    elif val > (75) and val < (90):
        greenLed.value(0)
        yellowLed.value(1)
        redLed.value(0)
    elif val > 0 and val < (75):
        greenLed.value(1)
        yellowLed.value(0)
        redLed.value(0)
    time.sleep(0.5)