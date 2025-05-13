# main.py
import threading
import time
import camera
import servo

def servo_loop():
    last_label = ""
    while True:
        label = camera.get_last_detected_label()
        if label != last_label and label in ["Criollo", "Forastero", "Trinitario"]:
            servo.rotate_servo_based_on_label(label)
            time.sleep(2)
            servo.set_angle(0)  # Return to 0° after action
            last_label = label
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        # Start servo loop in background
        threading.Thread(target=servo_loop, daemon=True).start()

        # Run GUI (must be in main thread)
        camera.start_gui()

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        servo.cleanup()
