from machine import Pin
import time

led = Pin(12,Pin.OUT)
while True:
    cmd = input("What is your command? (ON/OFF/TOGGLE) ")
    cmd = cmd.lower()
    if cmd == 'on':
        led.value(1)
    elif cmd == 'off':
        led.value(0)
    elif cmd == 'toggle':
        led.toggle()
    else:
        print("Incorrect command. Try again!")