from States import Color
from SafetyMonitor import SafetyMonitor

class TrafficLight:
    def __init__(self, name):
        # internal states
        self.name = name
        self.light = Color.R
        self.cars_waiting = 0

        self.safety_monitor = SafetyMonitor(self.name, self.light)

    def emit_output(self):
        light_out = self.light
        cars_waiting_out = self.cars_waiting
        return light_out, cars_waiting_out
    
    def handle_input(self, input):
        control, cars_arriving = input
        self.light = control
        self.cars_waiting += cars_arriving

        if self.light == Color.G:
            self.cars_waiting = max(self.cars_waiting - 3, 0)

        