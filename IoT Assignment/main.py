import tkinter as tk
import random
import time
from MonitoringDashboard import SmartHomeDashboard
from SmartLight import SmartLight
from Thermostat import Thermostat
from SecurityCamera import SecurityCamera
from AutomationSystem import AutomationSystem


# Create a Tkinter window
window = tk.Tk()

# Create an instance of the SmartHomeDashboard class
smart_home_dashboard = SmartHomeDashboard(window)

# Start the GUI main loop

window.mainloop()




