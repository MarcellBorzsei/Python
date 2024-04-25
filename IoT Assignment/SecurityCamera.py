import random
import time

class SecurityCamera:
    def __init__(self, device_id, light_reference):
        self.device_id = device_id
        self.status = False
        self.security_status = False
        self.detected_motion = False
        self.light_reference = light_reference

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def toggle(self):
        self.status = not self.status 

    def get_status(self):
        return "ON" if self.status else "OFF"

    def get_device_id(self):
        return self.device_id

    def get_security_status(self):
        return "ON" if self.security_status else "OFF"

    def turn_on_security_status(self):
        self.security_status = True

    def turn_off_security_status(self):
        self.security_status = False

    def turn_on_connected_light(self):
        self.light_reference.turn_on()
        self.light_reference.set_brightness(100)

    def simulate_random_motion(self):
        if self.status:
            if random.random() < 0.5:
                self.turn_on_security_status()
                self.light_reference.turn_on()

                self.light_reference.set_brightness(100)
                self.detected_motion = True
                return True
            else:
                self.detected_motion = False
                self.turn_off_security_status()
        return False
