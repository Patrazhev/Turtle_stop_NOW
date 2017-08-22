#!/usr/bin/env python

#import the dependencies
import roslib
import rospy

#import the kobuki messages
from kobuki_msgs.msg import ButtonEvent
from kobuki_msgs.msg import MotorPower
from kobuki_msgs.msg import Led

class Kill_switchP1V3:

    def __init__(self):
        #constructor
        rospy.init_node('Kill_switchP1V3')
        self.button_sub = rospy.Subscriber('mobile_base/events/button',
        ButtonCallback,self.ButtonEventCallback,queue_size = 1)

        self.led_pub = rospy.Publisher('mobile_base/commands/led2',Led)
        self.motor_pub = rospy.Publisher('mobile_base/commands/motor_power',
        MotorPower)
        self.state_count = 0
        self.led_pub.publish(1)
        self.motor_pub.publish(1)

    def __del__(self):
        self.led_pub.publish(0)


    def ButtonEventCallback(self,data):
        if ( data.state == ButtonEvent.RELEASED ):
                self.state = "released"
        else:
                self.state = "pressed"
                #update the state_count variable
                #execute the code here
                if self.state_count == 0:
                    #Red LED and motor off
                    self.led_pub.publish(3)
                    self.motor_pub.publish(0)
                    self.state_count = 1
                    rospy.loginfo('Motors have been halted')
                else:
                    #Green LED and Motor on
                    self.led_pub.publish(1)
                    self.motor_pub.publish(1)
                    self.state_count = 0
                    rospy.loginfo('Motors have been activated')

def main():
    KsP1V3 = Kill_switchP1V3()
    rospy.loginfo('Deadman switch is active')
    rospy.spin()

if __name__ == '__main__':
    main()
