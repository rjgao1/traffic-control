from Color import Color

class TrafficLight:
    def __init__(self):
        # internal states
        self.light = Color.R
        self.carsWaiting = 0

        # output variables
        self.lightOut = None
        self.carsWaitingOut = None


    def emit_output(self):
        lightOut = self.light
        carsWaitingOut = self.carsWaiting
        return lightOut, carsWaitingOut
    
    # input for TrafficLight = (control, carsArriving)
    # input for Controller = [(), (), (), ()]
    
    def handle_input(self, input):
        control, carsArriving = input
        self.light = control
        self.carsWaiting += carsArriving

        if self.light == Color.G:
            self.carsWaiting = max(self.carsWaiting - 3, 0)

        