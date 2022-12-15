from enum import Enum

class Color(Enum):
    R = 1
    G = 2
    Y = 3

class SafetyState(Enum):
    StateRed = 1
    StateGreen = 2
    StateYellow = 3
    Danger = 4