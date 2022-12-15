from States import Color

class TrafficLightController:
    def __init__(self):
        self.north = Color.G
        self.south = Color.G
        self.east = Color.R
        self.west = Color.R

        self.clock = 0

    def emit_output(self):
        controlNorth = self.north
        controlSouth = self.south
        controlEast = self.east
        controlWest = self.west
        return controlNorth, controlSouth, controlEast, controlWest
    
    def update_clock(self):
        self.clock += 1
    
    def handle_input(self, input):
        northInfo, southInfo, eastInfo, westInfo = input

        lightNorth, carsNorth = northInfo
        lightSouth, carsSouth = southInfo
        lightEast, carsEast = eastInfo
        lightWest, carsWest = westInfo

        if lightNorth == Color.Y or lightSouth == Color.Y:
            self.north = Color.R
            self.south = Color.R
            self.east = Color.G
            self.west = Color.G

        if lightNorth == Color.Y or lightSouth == Color.Y:
            self.north = Color.G
            self.south = Color.G
            self.east = Color.R
            self.west = Color.R

        if (carsNorth > 0 or carsSouth > 0) and (self.clock % 3 < 2):
            if lightEast == Color.G or lightSouth == Color.G:
                self.east = Color.Y
                self.west = Color.Y
        elif (carsEast > 0 or carsWest > 0):
            if lightNorth == Color.G or lightSouth == Color.G:
                self.north = Color.Y
                self.south = Color.Y
        elif lightEast == Color.G or lightWest == Color.G:
            self.east = Color.Y
            self.west = Color.Y