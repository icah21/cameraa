# servo.py
import RPi.GPIO as GPIO
import time

SERVO_PIN = 12  # GPIO12 = Pin 32 (not GPIO 18/17/23/24/25 as they're occupied)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz
pwm.start(0)

angle_map = {
    "Forastero": 90,
    "Criollo": 180,
    "Trinitario": 270
}

def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

def rotate_based_on_label(label):
    if label in angle_map:
        set_angle(angle_map[label])
        print(f"Servo rotated to {angle_map[label]}° for {label}")
    else:
        print("Unknown label. No movement.")

def cleanup():
    pwm.stop()
    GPIO.cleanup()
