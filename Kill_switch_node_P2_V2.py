import roslib
import rospy
#import the kobuki messages
from kobuki_msgs.msg import ButtonEvent
from kobuki_msgs.msg import MotorPower
from kobuki_msgs.msg import Led
from sensor_msgs.msg import Joy
class Kill_switch_P2_V2:

    def __init__(self):
            rospy.init_node("Kill_switch_P2_V2")
            #subscriber: logitech ButtonEvent red
            self.button_sub = rospy.Subscriber('/mobile_base/events/button',
            ButtonCallback,self.ButtonEventCallback,queue_size = 1)

            self.joy_sub = rospy.Subscriber('/joy',Joy,selfJoyEventCallback,
            queue_size = 1)
            #publishers: led2, cmd_vel_mux
            self.led_pub = rospy.Publisher("/mobile_base/commands/led2",
            /kobuki_msgs.msg.Value,queue_size=10)

            self.motor_pub = rospy.Publisher('/mobile_base/commands/motor_power',
            MotorPower, queue_size = 10)

            #state variable to keep track of what state
            # the robot is in.
            self.Kill_off()

            #initialize the led and print a message

            def ButtonEventCallback(self, data):
                if ( data.state == ButtonEvent.RELEASED ):
                        self.state = "released"
                else:
                        self.state = "pressed"
                        #update the state_count variable
                        #execute the code here
                        if self.state_count == 0:
                            #Red LED and motor off
                            self.Kill_on()
                        else:
                            #Green LED and Motor on
                            self.Kill_off()

            def JoyEventCallback(self, data):
                if data.buttons(2) = 1:
                    #start by the same as the button
                    self.Kill_on()

                    #execute code to stop the motors
                else:
                    self.Kill_off()


            def Kill_on(self):
                self.led_pub.publish(3)
                self.motor_pub.publish(0)
                self.state_count = 1
                rospy.loginfo('Motors have been halted')

            def Kill_off(self):
                self.led_pub.publish(1)
                self.motor_pub.publish(1)
                self.state_count = 0
                rospy.loginfo('Motors have been activated')
##################################################################

def Kill_switch_on():
    K_S = Kill_switch_P2_V2()


if __name__ == '__main__':
    try:
        Kill_switch_on()
        rospy.spin()

    except:rospy.ROSInterruptException:
            rospy.loginfo("exception")
