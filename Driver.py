from States import SafetyState
from TrafficLight import TrafficLight
from TrafficLightController import TrafficLightController
import random
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--carsReleased", type=int, default=5, help="max number of cars released by a traffic light in a clock cycle")
parser.add_argument("--maxClock", type=int, default=30, help="number of clock cycles to run")
parser.add_argument("--minCarsArriving", type=int, default=0, help="min number of cars arriving at a traffic light in a clock cycle")
parser.add_argument("--maxCarsArriving", type=int, default=3, help="max number of cars arriving at a traffic light in a clock cycle")
parser.add_argument("--buggyController", action="store_true", help="whether or not to execute buggy controller that will cause the safety monitor to fault")
parser.add_argument("--sleep", action="store_true", help="if set, sleep for 1 second between each clock cycle")

args = parser.parse_args()

# generate traffic load
# orchestrate interactions
# visualize/print states

# input for TrafficLight = (control, carsArriving)
# output for TrafficLight = (lightOut, carsWaitingOut)
# input for Controller = [(), (), (), ()]
# ouput for Controller = (controlNorth, controlSouth, controlEast, controlWest)

CLOCK = 0
MAX_CLOCK = args.maxClock
MIN_CAR_ARRIVING, MAX_CAR_ARRIVING = args.minCarsArriving, args.maxCarsArriving

controller = TrafficLightController(args.buggyController)
traffic_light_north = TrafficLight("North", args.carsReleased)
traffic_light_south = TrafficLight("South", args.carsReleased)
traffic_light_east = TrafficLight("East", args.carsReleased)
traffic_light_west = TrafficLight("West", args.carsReleased)
traffic_lights = [traffic_light_north, traffic_light_south, traffic_light_east, traffic_light_west]

def print_states(cars):
    print(f"clock: {CLOCK}")
    print(f"                        NORTH: {traffic_light_north.light.name}, cars: {cars[0]} arriving, {traffic_light_north.cars_waiting} remaining           ")
    print("\n")
    print(f"WEST: {traffic_light_west.light.name}, cars: {cars[3]} arriving, {traffic_light_west.cars_waiting} remaining            EAST: {traffic_light_east.light.name}, cars: {cars[2]} arriving, {traffic_light_east.cars_waiting} remaining")
    print("\n")
    print(f"                        SOUTH: {traffic_light_south.light.name}, cars: {cars[1]} arriving, {traffic_light_south.cars_waiting} remaining            ")
    print("\n\n")

def format_safety_monitor_outputs(output, name):
    if name == "North":
        return output[0], output[2], output[3]
    if name == "South":
        return output[1], output[2], output[3]
    if name == "East":
        return output[2], output[0], output[1]
    if name == "West":
        return output[3], output[0], output[1]

def execute_driver():
    global CLOCK, MAX_CLOCK, MIN_CAR_ARRIVING, MAX_CAR_ARRIVING

    cars = [0, 0, 0, 0] 
    while CLOCK < MAX_CLOCK:
        # all components emit outputs
        controller_out = controller.emit_output()
        traffic_light_outputs = [traffic_light.emit_output() for traffic_light in traffic_lights]
        
        if args.sleep:
            time.sleep(1)
        print_states(cars)
        
        # all components handle input
        # make carsArriving for each traffic light
        cars = [random.randint(MIN_CAR_ARRIVING, MAX_CAR_ARRIVING) for _ in range(4)]
        # all TrafficLight components handle input
        for i in range(len(traffic_lights)):
            # If everything is good, move on
            traffic_lights[i].handle_input((controller_out[i], cars[i]))
            
        for i in range(len(traffic_lights)):
            # Check safety monitor of each traffic light
            if traffic_lights[i].safety_monitor.update_state(format_safety_monitor_outputs(controller_out, traffic_lights[i].name)) == SafetyState.Danger:
                print("Traffic Light Simulation has reached Danger state. Halting simulation...")
                print("State at time of Error:")
                print_states(cars)
                return
        # Controller component handle input
        controller.handle_input(traffic_light_outputs)

        # advance clock
        CLOCK += 1
        controller.update_clock()

execute_driver()






