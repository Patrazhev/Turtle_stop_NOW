#!/usr/bin/env python

#import the dependencies
import roslib; roslib.load_manifest('kobuki_testsuit')
import rospy
import
#import the kobuki messages
from kobuki_msgs.msg import ButtonEvent
from kobuki_msgs.msg import MotorPower
from kobuki_msgs.msg import Led
from geometry_msgs.msg import Twist

## need to import the messages from JOY

#write the callback functions for each of the messages

def ButtonEventCallback(data):
        if ( data.state == ButtonEvent.RELEASED ):
                state = "released"
        else:
                state = "pressed"
        if ( data.button == ButtonEvent.Button0 ) :
                button = "B1"
        else:
                button = "B2"
def JoyEventCallback(data):
    if data.buttons(2) = 1:
        #red button is pressed
        red_button = 1

    else:
        red_button = 0

    #this is the callback for the joy messages
    #Joy sends out 2 fields in the messages:
    #axes & buttons; we dont care about axes

def Kill_switchP2V1():

        if state = "pressed":
            if state_count = 0:
                #this is change to the kill mode

                #publish Led
                led_pub.publish(kobuki_msgs.msg.Value(1))
                # x field data.linear.x -> this is how you would publish too the
                # cmd_vel_mux node
    return none

def Kill_switchP2V1_initialization():

        rospy.init_node("Kill_switchP2V1")
        #initializes subscriber and publishers
        #subscriber: logitech ButtonEvent red

        #publishers: led2, cmd_vel_mux
        led_pub = rospy.Publisher("/mobile_base/commands/led2",/kobuki_msgs.msg.Value,queue_size=10)
        cmd_vel_mux_pub = rospy.Publisher("/cmd_vel_mux/input/safety_controller",/)
        #state variable to keep track of what state
        # the robot is in.
        state_count = 0


        return none



 ## Main function starts HERE ##
if __name__ == '__main__':
    try:

        Kill_switchP2V1_initialization()

        Kill_switchP2V1


    except:rospy.ROSInterruptException:
            rospy.loginfo("exception")
