# Mobile Manipulator Simulation
The aim of this project is to simulate a simple pick and place scenario using a mobile manipulator. The simulation is performed using ROS and gazebo.

## Prerequisites
1. Ubuntu.
2. Robot Operating System (ROS) supported by your ubuntu version.

## Setup
1. Create a catkin workspace following this [tutorial](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
2. Install Moveit! package to your workspace following this [tutorial](https://moveit.ros.org/install/)

## Simulation
1. Navigate into your catkin workspace (catkin_ws, for example):
```
cd ~/catkin_ws
```
2. Build your catkin workspace:
```
catkin_make clean && catkin_make
```
3. Start up ROS master and ROS parameter server:
```
roscore
```
4. Launch the robot in the gazebo environment and start the controllers:
```
roslaunch robot_moveit_config robot_start_gazebo.launch
```
5. Launch moveit controller manager and move group interface:
```
roslaunch robot_moveit_config robot_moveit.launch
```
6. Move the robot to the desired location by publishing velocities to the controller:
```
rosrun rqt_robot_steering rqt_robot_steering
```
7. After reaching the desired position, start the pick-up operation:
```
rosrun robot_moveit_config move_to_pick.py
```
8. After pick-up, place the object on the mobile base:
```
rosrun robot_moveit_config move_to_home.py
```
9. Move the robot to the desired place position and place it on the ground following steps 6 and 7.
