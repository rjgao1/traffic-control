from States import SafetyState, Color

class SafetyMonitor:
    def __init__(self, name, startingState):
        self.name = name
        self.state = SafetyState(startingState.value)

    def update_state(self, input):
        currLight, opposingLight1, opposingLight2 = input

        print(f"Traffic Light {self.name}: {currLight.name}, {opposingLight1.name}, {opposingLight1.name}")
        if self.state == SafetyState.StateRed:
            self.state = SafetyState.StateGreen if currLight == Color.G else self.state
        elif self.state == SafetyState.StateGreen:
            if currLight == Color.R or opposingLight1 != Color.R or opposingLight2 != Color.R:
                self.state = SafetyState.Danger 
                print(f"Traffic Light {self.name} has entered the danger state!")
            elif currLight == Color.Y:
                self.state = SafetyState.StateYellow
        elif self.state == SafetyState.StateYellow:
            if opposingLight1 != Color.R or opposingLight2 != Color.R:
                self.state = SafetyState.Danger
                print(f"Traffic Light {self.name} has entered the danger state!")
            elif currLight == Color.R:
                self.state = SafetyState.StateRed
        
        return self.state