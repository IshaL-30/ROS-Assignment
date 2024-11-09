#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_rectangular_path():
    # Initialize the node
    rospy.init_node('move_rectangular_path', anonymous=True)
    
    # Create a publisher to publish velocity commands
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Create a Twist message instance
    move_cmd = Twist()
    
    # Set the speed of the turtle
    move_cmd.linear.x = 2  # speed in x (forward)
    move_cmd.angular.z = 0  # no rotation
    
    # Length and width of the rectangle (can be adjusted)
    length = 5  # meters
    width = 3  # meters
    
    # Loop to make the turtle move in a rectangle
    rate = rospy.Rate(1)  # 1 Hz
    for _ in range(2):  # Repeat twice to create a rectangle
        # Move straight
        rospy.loginfo("Moving straight for length")
        pub.publish(move_cmd)
        rospy.sleep(length / move_cmd.linear.x)
        
        # Stop for a moment before turning
        move_cmd.linear.x = 0
        pub.publish(move_cmd)
        rospy.sleep(1)
        
        # Turn 90 degrees
        move_cmd.angular.z = 1.57  # 90 degrees in radians
        pub.publish(move_cmd)
        rospy.sleep(1)
        
        # Move straight along width
        move_cmd.angular.z = 0
        move_cmd.linear.x = 2  # Reset speed
        pub.publish(move_cmd)
        rospy.sleep(width / move_cmd.linear.x)
        
        # Stop before turning
        move_cmd.linear.x = 0
        pub.publish(move_cmd)
        rospy.sleep(1)
        
        # Turn 90 degrees again to continue the rectangle
        move_cmd.angular.z = 1.57
        pub.publish(move_cmd)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        move_rectangular_path()
    except rospy.ROSInterruptException:
        pass
