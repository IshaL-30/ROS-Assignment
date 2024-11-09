# ROS Turtlesim Rectangular Path Movement

## Screen Recording
    https://www.canva.com/design/DAGV_nt3tRU/Wub8gI8VYcIyq47w3VECuw/watch?utm_content=DAGV_nt3tRU&utm_campaign=designshare&utm_medium=link&utm_source=editor

## Objective

The objective of this project is to control the movement of a turtle in the Turtlesim package to follow a rectangular path. The project demonstrates how to use ROS packages, nodes, subscribers, publishers, messages, and topics to make a turtle move in a controlled environment.

### Features:
- Turtlesim node initialization
- Control turtle's movement with velocity commands
- Move in a rectangular path
- Use ROS publishers and messages to send movement commands

---

## Installation

Follow the steps below to install the required dependencies and run the project:

### Prerequisites
- ROS Noetic installed
- Turtlesim package installed

### Step 1: Install ROS Noetic and Turtlesim

If you haven't installed ROS Noetic and the Turtlesim package, use the following commands:

```bash
sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install ros-noetic-turtlesim
```

### Step 2: Create a Catkin Workspace

Create a ROS workspace to hold your project:

```bash
mkdir -p ~/ros_ws/src
cd ~/ros_ws/src
catkin_init_workspace
cd ~/ros_ws
catkin_make
source devel/setup.bash
```

### Step 3: Clone the Repository

Clone this repository to the `src` directory of your workspace:

```bash
cd ~/ros_ws/src
git clone https://github.com/IshaL-30/ROS-Assignment
cd ~/ros_ws
catkin_make
source devel/setup.bash
```

---

## Usage

### Step 1: Start ROS Core

In one terminal, start the ROS core:

```bash
roscore
```

### Step 2: Launch Turtlesim

In another terminal, run the turtlesim node:

```bash
rosrun turtlesim turtlesim_node
```

### Step 3: Run the Rectangular Movement Code

In a third terminal, run the script to make the turtle move in a rectangular path:

```bash
rosrun move_turtle move_rectangular_path.py
```

The turtle will move in a rectangular path with adjustable length and width.

---

## Code Description

The main logic of moving the turtle in a rectangular path is contained in the Python script `move_rectangular_path.py`. The code:

- Initializes a ROS node `move_rectangular_path`
- Publishes velocity commands using the `Twist` message
- Moves the turtle in a rectangular path by adjusting the linear speed (forward movement) and angular velocity (turning)

The turtle first moves along the length of the rectangle, then turns 90 degrees, moves along the width, and repeats this process to complete the rectangular path.

---

## Dependencies

- `rospy`: ROS Python client library
- `geometry_msgs`: For publishing movement commands
