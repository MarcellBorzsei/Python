import random
import time

class SmartLight:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False
        self.brightness = 0

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def get_status(self):
        return "ON" if self.status else "OFF"

    def get_device_id(self):
        return self.device_id

    def get_brightness(self):
        return self.brightness
    
    def toggle(self):
        self.status = not self.status

    def set_brightness(self, new_brightness):
        self.brightness = new_brightness

    def gradual_dimming(self, wanted_brightness):
        wanted_brightness = int(wanted_brightness)
        if self.status:
            step = 1
            while self.brightness != wanted_brightness:
                if self.brightness > wanted_brightness:
                    self.brightness = max(wanted_brightness, self.brightness - step)
                else:
                    self.brightness = min(wanted_brightness, self.brightness + step)
                time.sleep(1)

    def simulate_random_changes(self):
        if self.status:
            while 0 < self.brightness < 100:
                self.brightness += random.uniform(-5, 5)
                self.brightness = max(0, min(100, self.brightness))
                time.sleep(1)
            return True  # when the device is active
        return False  # when the device is off
