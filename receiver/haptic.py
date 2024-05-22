import RPi.GPIO as GPIO
HAPTIC_PIN = 00
def setup(pin):
    PIN = pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(HAPTIC_PIN, GPIO.OUT)
    global p



def run(duty):
    global p
    p = GPIO.PWM(HAPTIC_PIN, p)
    p.start(1)

def stop():
    global p
    p.stop()