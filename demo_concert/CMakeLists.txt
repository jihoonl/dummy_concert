cmake_minimum_required(VERSION 2.8.3)
project(demo_concert)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  concert_master
  rospy
)

# find_package(Boost REQUIRED COMPONENTS system)
# catkin_python_setup()

catkin_package(
)
