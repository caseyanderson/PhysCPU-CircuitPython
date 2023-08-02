#change the LED light brightness through the value of distance sensor US100
#Another light will on when you're out of range

import time

import board
import busio
import adafruit_us100

import pwmio

#distance
led = pwmio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
#out of range
led2 = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)


uart = busio.UART(board.TX, board.RX, baudrate=9600)
us100 = adafruit_us100.US100(uart)


while True:
    print("-----")
    val = us100.distance
    # print("Temperature: ", us100.temperature)
    # time.sleep(0.5)
    # print("Distance: ", val)
    print(led.duty_cycle / 65535)
    if val > 1100:
        led.duty_cycle = 0
        led2.duty_cycle = 65535
    elif val % 100 < 50:
        led.duty_cycle = 65535 - int(val % 100 / 100 * 65535)
        led2.duty_cycle = 0
    else:
        led.duty_cycle = int( val % 100 / 100 * 65535)
        led2.duty_cycle = 0

    time.sleep(0.01)
