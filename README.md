# SRC2-move_base

This topic depend on: 
src2_driving
gazebo_truth_odom

List of topics to launch in round 1 to test.

roslaunch driving_control scout_driving_control.launch 
roslaunch gazebo_truth_odom ground_truth.launch 
rosrun src2_move_base world_frame_publisher.py 
	
rosrun map_server map_server map.yaml  # map_server from yaml and pgm file, or run mapless move_base
roslaunch src2_move_base move_base.launch 

rviz # load the rviz from the src2_move_base rviz folder
rqt # to run dynamic reconfigure to tune move_base

