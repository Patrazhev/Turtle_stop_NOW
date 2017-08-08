#!/usr/bin/env python

#import the dependencies
import roslib; roslib.load_manifest('kobuki_testsuit')
import rospy

#import the kobuki messages
from kobuki_msgs.msg import ButtonEvent
from kobuki_msgs.msg import MotorPower
from kobuki_msgs.msg import Led
#write the callback functions for each of the messages

#this can be implemented in the form of a class. think about it and
# make it happen tomorrow.


def ButtonEventCallback(data):
        if ( data.state == ButtonEvent.RELEASED ):
                state = "released"
        else:
                state = "pressed"
        if ( data.button == ButtonEvent.Button0 ) :
                button = "B1"
        else:
                button = "B2"


def Kill_switchP1V1():
    rospy.init_node("Kill_switchP1V1") #initializes the node
    rospy.loginfo('node initilized')
    rospy.Subscriber("/mobile_base/events/button",ButtonEvent,ButtonEventCallback) #subscribes

    state_count = 0 # initializes the state variable
    #creates the publishers

    motor_pub = rospy.Publisher("/mobile_base/commands/motor_power",/kobuki_msgs.msg.MotorPower,queue_size=10)
    led_pub = rospy.Publisher("/mobile_base/commands/Led",/kobuki_msgs.msg.Value,queue_size=10)
    
    # pass LED message == 1
    led_pub.publish(kobuki_msgs.msg.Value(1))
    #start the if loop
    if state = 'pressed':  #button event registered
            rospy.loginfo("Button Press detected")
            if state_count = 0:
                    #pass the LED message == 3
                    led_pub.publish(kobuki_msgs.msg.Value(3))
                    #pass the motor message == 0
                    motor_pub.publish(kobuki_msgs.msg.state(0))
                    state_count = 1
            else:
                    #pass LED message == 1
                    led_pub.publish(kobuki_msgs.msg.Value(1))
                    #pass Motor message == 1
                    motor_pub.publish(kobuki_msgs.msg.state(1))
                    state_count = 0
    else:

    rospy.spin() #this keep the code running until you press ctrl+c

#begin the main function

if __name__ == '__main__':
        try:
            Kill_switchP1V1()

        except rospy.ROSInterruptException:
                rospy.loginfo("exception")
