from States import SafetyState
from TrafficLight import TrafficLight
from TrafficLightController import TrafficLightController
import random
import time

# generate traffic load
# orchestrate interactions
# visualize/print states

# input for TrafficLight = (control, carsArriving)
# output for TrafficLight = (lightOut, carsWaitingOut)
# input for Controller = [(), (), (), ()]
# ouput for Controller = (controlNorth, controlSouth, controlEast, controlWest)

CLOCK = 0
MAX_CLOCK = 30
MIN_CAR_ARRIVING, MAX_CAR_ARRIVING = 0, 3

controller = TrafficLightController()
traffic_light_north = TrafficLight("North")
traffic_light_south = TrafficLight("South")
traffic_light_east = TrafficLight("East")
traffic_light_west = TrafficLight("West")
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






