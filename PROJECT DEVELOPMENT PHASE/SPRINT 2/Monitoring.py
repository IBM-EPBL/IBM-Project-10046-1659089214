LED BLINKING:

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
cnt = 0
MAIL_CHECK_FREQ = 1
RED_LED = 4
GPIO.setup(RED_LED, GPIO.OUT)
while True:
 if cnt == 0 :
 GPIO.output(RED_LED, False)
 cnt = 1
 else:
 GPIO.output(RED_LED, True)
 cnt = 0
time.sleep(MAIL_CHECK_FREQ)
GPIO.cleanup()


CODE FOR TRAFFIC LIGHTS FOR RASPBERRY PI:

import RPi.GPIO as GPIO
import time
try:
 def lightTraffic(led1, led2, led3, delay ):
 GPIO.output(led1, 1)
 time.sleep(delay)
 GPIO.output(led1, 0)
 GPIO.output(led2, 1)
 time.sleep(delay)
 GPIO.output(led2, 0)
 GPIO.output(led3, 1)
 time.sleep(delay)
 GPIO.output(led3, 0)
 GPIO.setmode(GPIO.BCM)
 button = 19
 GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 ledGreen = 16
 ledYellow = 12
 ledRed = 23
 GPIO.setup(ledGreen, GPIO.OUT)
 GPIO.setup(ledYellow, GPIO.OUT)
 GPIO.setup(ledRed, GPIO.OUT)
 while True:
 input_state = GPIO.input(button)
 if input_state == False:
 print('Button Pressed')
 lightTraffic(ledGreen, ledYellow, ledRed, 1)
 else:
 GPIO.output(ledGreen, 0)
 GPIO.output(ledYellow, 0)
 GPIO.output(ledRed, 0)
except KeyboardInterrupt:
 print ("You've exited the program")
finally:
 GPIO.cleanup()
