import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)		# A
GPIO.setup(3, GPIO.OUT)		# B
GPIO.setup(17, GPIO.OUT)	# C
GPIO.setup(27, GPIO.OUT)	# DP
GPIO.setup(25, GPIO.OUT)	# D
GPIO.setup(24, GPIO.OUT)	# E
GPIO.setup(23, GPIO.OUT)	# F
GPIO.setup(22, GPIO.OUT)	# G
GPIO.setup(5, GPIO.OUT)		# Red LED A
GPIO.setup(12, GPIO.OUT)	# Yellow LED A
GPIO.setup(6, GPIO.OUT)		# Green LED A
GPIO.setup(13, GPIO.OUT)	# Red LED B
GPIO.setup(16, GPIO.OUT)	# Yellow LED B
GPIO.setup(26, GPIO.OUT)	# Green LED B


# Define 7 degment digits
gpio = [2, 3, 17, 27, 25, 24, 23, 22]
digitclr = [0, 0, 0, 0, 0, 0, 0, 0]
digit0 = [1, 1, 1, 0, 1, 1, 1, 0]
digit1 = [0, 1, 1, 0, 0, 0, 0, 0]
digit2 = [1, 1, 0, 0, 1, 1, 0, 1]
digit3 = [1, 1, 1, 0, 1, 0, 0, 1]
digit4 = [0, 1, 1, 0, 0, 0, 1, 1]
digit5 = [1, 0, 1, 0, 1, 0, 1, 1]
digit6 = [1, 0, 1, 0, 1, 1, 1, 1]
digit7 = [1, 1, 1, 0, 0, 0, 0, 0]

# Handles the digits to display
def display(digit):
   for x in range (0, 8):
     GPIO.output(gpio[x], digitclr[x])
   for x in range (0, 8):
     GPIO.output(gpio[x], digit[x])

while True:
    # Signal A (West-East)
    
    # Initial S0
    GPIO.output(6, 1)	# Green LED A on
    GPIO.output(26, 1)	# Red LED B on
    
    display(digit7)
    time.sleep(1)
    display(digit6)
    time.sleep(1)
    display(digit5)
    time.sleep(1)
    display(digit4)
    time.sleep(1)
    display(digit3)
    time.sleep(1)
    display(digit2)
    time.sleep(1)
    display(digit1)
    time.sleep(1)
    display(digit0)
    time.sleep(1)
    
    GPIO.output(6, 0)	# Green LED A off
    time.sleep(0.1)

    # S1
    GPIO.output(12, 1)	# Yellow LED A on
    
    display(digit2)
    time.sleep(1)
    display(digit1)
    time.sleep(1)
    display(digit0)
    time.sleep(1)
    
    GPIO.output(12, 0)	# Yellow LED A off
    time.sleep(0.1)

    # S2
    GPIO.output(5, 1)	# Red LED A on
    
    display(digit2)
    time.sleep(1)
    display(digit1)
    time.sleep(1)
    display(digit0)
    time.sleep(1)
    
    GPIO.output(26, 0)	# Red LED B off

    # Signal B (North-South)
    
    # S3
    GPIO.output(13, 1)	# Green LED B on
    GPIO.output(5, 1)	# Red LED A on

    display(digit7)
    time.sleep(1)
    display(digit6)
    time.sleep(1)
    display(digit5)
    time.sleep(1)
    display(digit4)
    time.sleep(1)
    display(digit3)
    time.sleep(1)
    display(digit2)
    time.sleep(1)
    display(digit1)
    time.sleep(1)
    display(digit0)
    time.sleep(1)
    
    GPIO.output(13, 0)	# Green LED B off
    time.sleep(0.1)

    # S4
    GPIO.output(16, 1)	# Yellow LED B on
    
    display(digit2)
    time.sleep(1)
    display(digit1)
    time.sleep(1)
    display(digit0)
    time.sleep(1)
    
    GPIO.output(16, 0)	# Yellow LED B off
    time.sleep(0.1)

    # S5
    GPIO.output(26, 1)	# Red LED B on
    
    display(digit2)
    time.sleep(1)
    display(digit1)
    time.sleep(1)
    display(digit0)
    time.sleep(1)
    
    GPIO.output(5, 0)	# Red LED A on

GPIO.cleanup()