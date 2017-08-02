# Turtle_stop_NOW
ROS nodes to implement a kill switch on the kobuki turtlebot V2

There will be 2 phases to the project: 
    Phase 1 = using the button on the turtlebot as the input and having the node kill power to the motor.
    
    Phase 2 = using a logitec gamepad as the input to the kill switch node nad then having the node publish
    on the velocity topic with highest priority. 
