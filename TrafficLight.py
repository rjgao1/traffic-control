from States import Color

class TrafficLight:
    def __init__(self):
        # internal states
        self.light = Color.R
        self.carsWaiting = 0

    def emit_output(self):
        lightOut = self.light
        carsWaitingOut = self.carsWaiting
        return lightOut, carsWaitingOut
    
    def handle_input(self, input):
        control, carsArriving = input
        self.light = control
        self.carsWaiting += carsArriving

        if self.light == Color.G:
            self.carsWaiting = max(self.carsWaiting - 5, 0)

        