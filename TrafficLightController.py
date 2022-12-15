from States import Color

class TrafficLightController:
    def __init__(self, buggy=False):
        self.north = Color.G
        self.south = Color.G
        self.east = Color.R
        self.west = Color.R

        self.clock = 0
        self.buggy = buggy

    def emit_output(self):
        control_north = self.north
        control_south = self.south
        control_east = self.east
        control_west = self.west
        return control_north, control_south, control_east, control_west
    
    def update_clock(self):
        self.clock += 1
    
    def handle_input(self, input):
        north_info, south_info, east_info, west_info = input

        light_north, cars_north = north_info
        light_south, cars_south = south_info
        light_east, cars_east = east_info
        light_west, cars_west = west_info

        if light_north == Color.Y or light_south == Color.Y:
            self.north = Color.R
            self.south = Color.R
            self.east = Color.G
            self.west = Color.G
            return

        if light_east == Color.Y or light_west == Color.Y:
            self.north = Color.G
            self.south = Color.G
            self.east = Color.R
            self.west = Color.R
            return

        if (cars_north > 0 or cars_south > 0) and (self.clock % 3 < 2):
            if not self.buggy:
                if light_east == Color.G or light_west == Color.G:
                    self.east = Color.Y
                    self.west = Color.Y
                return
            else:
                if light_east == Color.G or light_south == Color.G:
                    self.east = Color.Y
                    self.west = Color.Y
                return
        elif (cars_east > 0 or cars_west > 0):
            if light_north == Color.G or light_south == Color.G:
                self.north = Color.Y
                self.south = Color.Y
            return
        elif light_east == Color.G or light_west == Color.G:
            self.east = Color.Y
            self.west = Color.Y
            return