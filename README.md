# Traffic Light System Simulator
A simulation design for a two-lane, four-way traffic intersection that fulfills the safety and liveness requirements described. No prerequisites are required to run this project other than Python 3. 

Completed as a project for CS6376 at Vanderbilt University. 

## Running the Simulation 
Our simulation takes in five parameters that can be modified to customize the simulation. 
```
--carsReleased     The number of cars that can pass through the traffic light in one clock cycle. The default value is 5.
--minCarsArriving  The minimum numbers of cars to arrive at each traffic light in one clock cycle. The default value is 0. 
--maxCarsArriving  The maximum number of cars arriving at a traffic light in one clock cycle. The default value is 3.
--maxClock         The number of clock cycles for the simulation to run. The default value is 30. 
--sleep            In order to simulate the clock cycles, set this flag in order to sleep for 1 second between each clock cycle. 
```
Example:
```
python driver.py --carsReleased=10 --minCarsArriving=2 --maxCarsArriving=4 --maxClock=50 --sleep
```

We have also included a buggy implementation of the program (i.e. one that violates our safety requirements and will lead to a collision of cars) in order to demonstrate the implementation of our safety monitor. In order to utilize the buggy implementation, please set the ```--buggyController``` flag. This flag can also be utilized with the other parameters above.

Example:
```
python driver.py --buggyController
```

## Demonstration
For a full demonstration of the project, please see the video at [this](https://drive.google.com/file/d/1-j5qRbQzBK70xZInog8nXMkgSFViMUpY/view?usp=sharing) link.