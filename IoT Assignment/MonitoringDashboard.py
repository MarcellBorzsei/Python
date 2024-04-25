import tkinter as tk
import threading
import time
from SmartLight import SmartLight
from Thermostat import Thermostat
from SecurityCamera import SecurityCamera
from AutomationSystem import AutomationSystem

class SmartHomeDashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("Smart Home Monitoring Dashboard")
        self.window.geometry("800x600")

        self.light1 = SmartLight("Light1")
        self.thermostat1 = Thermostat("Thermostat1")
        self.camera1 = SecurityCamera("Camera1", self.light1)

        self.label_light = tk.Label(window, text="Light: OFF")
        self.label_thermostat = tk.Label(window, text="Thermostat: OFF")
        self.label_camera = tk.Label(window, text="Camera: OFF")

        self.label_automation_rule = tk.Label(
            window, text="Automation Rule: Turn on lights when motion is detected and camera is on"
        )
        self.label_automation_rule.pack(pady=10)

        self.button_toggle_light = tk.Button(window, text="Toggle Light", command=self.toggle_light)
        self.button_toggle_thermostat = tk.Button(window, text="Toggle Thermostat", command=self.toggle_thermostat)
        self.button_toggle_camera = tk.Button(window, text="Toggle Camera", command=self.toggle_camera)
        self.button_random_motion_detector = tk.Button(window, text="Detect Random Motion", command=self.detect_random_motion)

        self.brightness_scale = tk.Scale(window, from_=0, to=100, orient="horizontal", label="Brightness", command=self.control_brightness)
        self.temperature_scale = tk.Scale(window, from_=0, to=100, orient="horizontal", label="Temperature", command=self.control_temperature)

        self.log_text = tk.Text(window, height=10, width=40)
        self.log_text.config(state=tk.DISABLED)

        self.label_light.pack()
        self.label_thermostat.pack()
        self.label_camera.pack()
        self.button_toggle_light.pack()
        self.button_toggle_thermostat.pack()
        self.button_toggle_camera.pack()
        self.button_random_motion_detector.pack()
        self.brightness_scale.pack()
        self.temperature_scale.pack()
        self.log_text.pack()

        self.automation_system = AutomationSystem(self.label_light, self.log_text, self.brightness_scale)
        self.automation_system.add_device(self.light1)
        self.automation_system.add_device(self.thermostat1)
        self.automation_system.add_device(self.camera1)
        self.start_simulation()

   

    def update_label_text(self, widget, message):
        if isinstance(widget, tk.Label):
            widget.config(text=message)
        elif isinstance(widget, tk.Text):
            widget.config(state=tk.NORMAL)  # Enable text widget for editing
            widget.delete(1.0, tk.END)  # Clear existing content
            widget.insert(tk.END, message)  # Insert new message
            widget.config(state=tk.DISABLED)  # Disable text widget to make it read-only
        else:
            print(f"Warning: Attempted to update text on an unsupported widget: {widget}")

    
    
    def update_labels_and_log(self, device):
        try:
            if device.get_device_id() == "Light1":
                status_message = f"Light: {device.get_status()}"
                self.schedule_label_update(self.label_light, status_message)
                
                # Enable or disable brightness scale based on light status
                self.brightness_scale.set(device.get_brightness())
                self.brightness_scale.config(state=tk.NORMAL if device.get_status() else tk.DISABLED)

            elif device.get_device_id() == "Thermostat1":
                status_message = f"Thermostat: {device.get_status()}"
                self.schedule_label_update(self.label_thermostat, status_message)
                
                # Enable or disable temperature scale based on thermostat status
                self.temperature_scale.set(device.get_temperature())
                self.temperature_scale.config(state=tk.NORMAL if device.get_status() else tk.DISABLED)

            elif device.get_device_id() == "Camera1":
                status_message = f"Camera: {device.get_status()}"
                self.schedule_label_update(self.label_camera, status_message)
        except Exception as e:
            error_message = f"Error updating {device.get_device_id()} labels: {e}"
            self.schedule_label_update(self.log_text, error_message)

    def schedule_label_update(self, widget, message):
        self.window.after(0, lambda: self.update_label_text(widget, message))

    def control_brightness(self, value):
        if self.light1.get_status() == "ON":
            new_brightness = int(self.brightness_scale.get())
            self.light1.set_brightness(new_brightness)
            brightness_message = f"Brightness set to: {self.light1.get_brightness()}"
            self.schedule_label_update(self.log_text, brightness_message)
            
        
        # Update the labels and log only if the brightness value changes
        #if int(value) != self.light1.get_brightness():
         #   if self.light1.get_status():
          #      self.light1.set_brightness(value)
           #     self.update_labels_and_log(self.light1)

    def control_temperature(self, value):
        if self.thermostat1.get_status() == "ON":
            new_temperature = int(self.temperature_scale.get())
            self.thermostat1.set_temperature(new_temperature)
            temperature_message = f"Temperature set to: {value}"
            self.schedule_label_update(self.log_text, temperature_message)

        

    def toggle_light(self):
        self.light1.toggle()
        self.update_labels_and_log(self.light1)
        if self.light1.status == True:
            brightness_message = f"Light: ON"
            self.schedule_label_update(self.log_text, brightness_message)
        else:
            brightness_message = f"Light: OFF"
            self.schedule_label_update(self.log_text, brightness_message)
            
    def toggle_thermostat(self):
        self.thermostat1.toggle()
        self.update_labels_and_log(self.thermostat1)
        if self.thermostat1.status == True:
            brightness_message = f"Thermostat: ON"
            self.schedule_label_update(self.log_text, brightness_message)
        else:
            brightness_message = f"Thermostat: OFF"
            self.schedule_label_update(self.log_text, brightness_message)

    def toggle_camera(self):
        self.camera1.toggle()
        self.update_labels_and_log(self.camera1)
        if self.camera1.status == True:
            brightness_message = f"Camera: ON"
            self.schedule_label_update(self.log_text, brightness_message)
        else:
            brightness_message = f"Camera: OFF"
            self.schedule_label_update(self.log_text, brightness_message)

    def detect_random_motion(self):
        if self.camera1.get_status():
            if self.camera1.simulate_random_motion():
                motion_message = "Random Motion Detected!"
                self.brightness_scale.set(100)
            else:
                motion_message = "No motion detected."
            self.schedule_label_update(self.log_text, motion_message)
            self.update_labels_and_log(self.camera1)


    def start_simulation(self):
        time = 5000
        sleep = 5
        self.sim_thread = threading.Thread(target=self.automation_system.run_life_simulation, args=(time, sleep))
        self.sim_thread.daemon = True
        self.sim_thread.start()

# Assume you have the following classes defined in separate files: SmartLight, Thermostat, SecurityCamera, and AutomationSystem
