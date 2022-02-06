#!/usr/bin/env python3

from __future__ import print_function
# from six.moves import input

from os import wait
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi, tau, dist, fabs, cos, trunc
from std_msgs.msg import String
# from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_group_python_interface", anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher("/move_group/display_planned_path", moveit_msgs.msg.DisplayTrajectory, queue_size=20)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 0.0
joint_goal[1] = 0.56
joint_goal[2] = 1.76
joint_goal[3] = 0.0
joint_goal[4] = 0.81

plan = move_group.go(joint_goal, wait=True)
move_group.stop()
move_group.execute(plan, wait=True)

# joint_goal = move_group.get_current_joint_values()
# joint_goal[0] = 0.0
# joint_goal[1] = 0.0
# joint_goal[2] = 0.0
# joint_goal[3] = 0.0
# joint_goal[4] = 0.0

# plan = move_group.go(joint_goal, wait=True)
# move_group.stop()
# move_group.execute(plan, wait=True)

# pose_goal = geometry_msgs.msg.Pose()
# pose_goal.orientation.w = 0.700211
# pose_goal.position.x = -0.0129666
# pose_goal.position.y = -0.158827
# pose_goal.position.z = 0.366965

# move_group.set_pose_target(pose_goal)
# plan = move_group.go(wait=True)
# move_group.stop()
# move_group.clear_pose_targets()