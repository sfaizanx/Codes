import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

for i in range(10):
    
    GPIO.output(7, True)  # Turn on LED
    print("LED ON")
    time.sleep(1)  # Wait for 1 second

    GPIO.output(7, False)  # Turn off LED
    print("LED OFF")
    time.sleep(1)  # Wait for 1 second

print("Done")
GPIO.cleanup()
