#!/usr/bin/env python

#import the dependencies
import roslib; 
import rospy

#import the kobuki messages
from kobuki_msgs.msg import ButtonEvent
from kobuki_msgs.msg import MotorPower
from kobuki_msgs.msg import Led
#write the callback functions for each of the messages

class Kill_switchP1:

    def __init__(self):
                                        #constructor
        #initialize the subscribers
        #initialize the publishers
        self.button_sub = rospy.Subscriber("mobile_base/events/button",
        ButtonEvent,self.ButtonEventCallback,queue_size = 1)

        self.motor_pub = rospy.Publisher("/mobile_base/commands/motor_power",
        MotorPower)

        self.led_pub = rospy.Publisher("/mobile_base/commands/led2",Led)
        #initialize the hidden variables
        self.state = "initilized"
        self.state_count = 0
        self.led_pub.publish(1)



    def ButtonEventCallback(self, data):
        if ( data.state == ButtonEvent.RELEASED ):
                self.state = "released"
        else:
                self.state = "pressed"
        if ( data.button == ButtonEvent.Button0 ) :
                self.button = "B1"
        else:
                self.button = "B2"

    def safety_first(self):
        while not rospy.is_shutdown():
            if self.state == 'pressed':
                rospy.loginfo("Button Press Detected")
                if self.state_count == 0:
                    #Red LED and motor off
                    self.led_pub.publish(3)
                    self.motor_pub.publish(0)
                    self.state_count = 1
                else:
                    #Green LED and Motor on
                    self.led_pub.publish(1)
                    self.motor_pub.publish(1)
                    self.state_count = 0
                else:
            pass
####################################################################
def main(self):
    KsP1V2 = Kill_switchP1()
    rospy.init_node("Kill_switchP1V2") #initializes the node
    try:
        KsP1V2.safety_first()
    except:rospy.ROSInterruptException:
            rospy.loginfo("exception")

if __name__ == '__main__':
    main()
