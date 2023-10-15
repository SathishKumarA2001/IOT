import time
import RPi.GPIO as GPIO
from colour import Color
from threading import Thread

GPIO.setmode(GPIO.BOARD)

speed = 0.1

class RGB():
    def __init__(self, r, g, b):
        GPIO.setup([r, g, b], GPIO.OUT)
        self.r = GPIO.PWM(r, 120)
        self.g = GPIO.PWM(g, 120)
        self.b = GPIO.PWM(b, 120)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

    def setRGB(self, rgb):
        r = abs(rgb[0] * 100 - 100)
        g = abs(rgb[1] * 100 - 100)
        b = abs(rgb[2] * 100 - 100)
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))


stopThread = False
def rgb_transistion_thred():
    while not stopThread:
        for c in Color("red").range_to(Color("green"), 100):
            if stopThread: return
            led.setRGB(c.rgb)
            time.sleep(speed)
        for c in Color("red").range_to(Color("blue"), 255):
            if stopThread: return
            led.setRGB(c.rgb)
            time.sleep(speed)
        for c in Color("blue").range_to(Color("red"), 255):
            if stopThread: return
            led.setRGB(c.rgb)
            time.sleep(speed)

led = RGB(32, 33, 35)

thread1 = Thread(target=rgb_transistion_thred)
thread1.start()

inputchannel = 7
GPIO.setup(inputchannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(inputchannel, GPIO.RISING)

starttime = None
try: 
    while True:
        if GPIO.event_detected(inputchannel):            
            if starttime is None:
                starttime = time.time()

            if starttime is not None:
                speed = time.time() - starttime
                starttime = None
        print(speed)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    stopThread = True
    thread1.join()
    print("Cleaned up")

