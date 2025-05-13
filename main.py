# main.py
import threading
import time
from camera import start_gui, get_last_detected_label
from servo import rotate_based_on_label, cleanup

def monitor_servo():
    last_label = ""
    while True:
        current_label = get_last_detected_label()
        if current_label != last_label and current_label in ["Criollo", "Forastero", "Trinitario"]:
            rotate_based_on_label(current_label)
            last_label = current_label
        time.sleep(1)

if __name__ == "__main__":
    try:
        threading.Thread(target=monitor_servo, daemon=True).start()
        start_gui()
    except KeyboardInterrupt:
        cleanup()
