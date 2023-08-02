import time
import board
import pwmio
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D7)

led_1 = pwmio.PWMOut(board.A1)
led_2 = pwmio.PWMOut(board.D5)
detect_range = 200
dist = 0

while True:
    try:
        dist = sonar.distance
        if dist < detect_range:
            led_2.duty_cycle = 0
            # print((sonar.distance,))
            scale = int( (200 - dist) * 65535 / 199)
            scale_lable = " ".join(["scale:", str(scale/65535)])
            
            # print(scale_lable)
            led_1.duty_cycle = scale
        else:
            led_1.duty_cycle = 0
            led_2.duty_cycle = 65535
    except RuntimeError:
        print("Retrying!")
        led_1.duty_cycle = 0
        led_2.duty_cycle = 65535
    print(">scale:", led_1.duty_cycle/65535)
    time.sleep(0.1)