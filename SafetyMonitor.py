from States import SafetyState, Color

class SafetyMonitor:
    def __init__(self, name, startingState):
        self.name = name
        self.state = SafetyState(startingState.value).name

    def update_state(self, input):
        currLight, opposingLight1, opposingLight2 = input

        if self.state == SafetyMonitor.StateRed:
            self.state = SafetyState.StateGreen if currLight == Color.G else self.state
        elif self.state == SafetyMonitor.StateGreen:
            if currLight == Color.Y:
                self.state = SafetyState.StateYellow
            elif currLight == Color.R or opposingLight1 != Color.R or opposingLight2 != Color.R:
                self.state = SafetyState.Danger 
                print(f"Traffic Light {self.name} has entered the danger state!")
        elif self.state == SafetyMonitor.StateYellow:
            if currLight == Color.R:
                self.state = SafetyState.StateRed
            elif opposingLight1 != Color.R or opposingLight2 != Color.R:
                self.state = SafetyState.Danger
                print(f"Traffic Light {self.name} has entered the danger state!")
        
        return self.state