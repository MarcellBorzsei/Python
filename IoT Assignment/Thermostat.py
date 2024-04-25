import random
import time
class Thermostat:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False
        self.temperature = 0
        self.min_temperature = 0
        self.max_temperature = 100

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def get_status(self):
        return "ON" if self.status else "OFF"

    def get_device_id(self):
        return self.device_id

    def get_temperature(self):
        return self.temperature

    def get_min_temperature(self):
        return self.min_temperature

    def get_max_temperature(self):
        return self.max_temperature

    def toggle(self):
        self.status = not self.status

    def temp_range(self, min_temp, max_temp):
        self.min_temperature = min_temp
        self.max_temperature = max_temp

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

    def simulate_random_changes(self):
        if self.status:
            while self.status:
                temperature_change = random.uniform(-1, 1)
                self.temperature += temperature_change
                time.sleep(5)
            return True  # when the device is active
        return False  # when the device is not active

    
