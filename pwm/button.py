from time import sleep
import RPi.GPIO as GPIO

# class button:
#     def __init__(self, channel):
#         self.channel = channel
#         GPIO.setmode(GPIO.BOARD)
#         GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#     def __del__(self):
#         GPIO.cleanup()

#     def click(self):
#         while(True):
#             if GPIO.input(self.channel):
#                 print('Button pressed')
#                 sleep(0.2)


# button_instance = button(7)
# button_instance.click()


def my_callback_one(channel):
    print('Callback one')

def my_callback_two(channel):
    print('Callback two')

channel = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback_one, bouncetime=200)

while True:
    sleep(1)
    GPIO.event_detected(channel)

print("helo")