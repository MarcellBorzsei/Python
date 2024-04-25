from SecurityCamera import SecurityCamera
import time

class AutomationSystem:

    def __init__(self, lightLabel, log_text, brightness_scale):
        self.devices = []
        self.lightLabel = lightLabel
        self.log_text = log_text
        self.brightness_scale = brightness_scale
    
    def add_device(self, newDevice):
        self.devices.append(newDevice)

    def getDevices(self):
        return self.devices

    def run_life_simulation(self, dur, sleep_time):
        lastingTime = time.time() + dur

        while time.time() < lastingTime:
            for device in self.devices:
                if isinstance(device, SecurityCamera):
                    if device.status:
                        device.simulate_random_motion()
                        if device.detected_motion:
                            try:
                                self.lightLabel.config(text=f"Light: {device.light_reference.get_status()}")
                                self.brightness_scale.set(100)
                                self.brightness_scale.config(state=tk.NORMAL if device.get_status() else tk.DISABLED)
                            except:
                                pass
                
            time.sleep(sleep_time)
