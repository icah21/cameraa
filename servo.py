# servo.py
import RPi.GPIO as GPIO
import time

SERVO_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

def rotate_servo_based_on_label(label):
    print(f"[Servo] Detected: {label}")
    if label == "Criollo":
        set_angle(45)
    elif label == "Forastero":
        set_angle(-45)
    elif label == "Trinitario":
        set_angle(0)
    else:
        print("[Servo] Unknown label, no action")

def cleanup():
    pwm.stop()
    GPIO.cleanup()
