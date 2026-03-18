# 🤖 HUMYNEX ROBOTICS 

MBOT: Unified ROS 2 Workspace

---

### 🏢 **Developed by HUMYNEX ROBOTICS**
**Mission:** Make your ideas into reality.  
**Contact:** [humynexrobotics@gmail.com](mailto:humynexrobotics@gmail.com) | **Phone:** +91 8714358646  

---

Welcome to the **MBOT** custom wheeled robot workspace! This platform is designed to be **hardware-agnostic**, supporting both **Arduino Nano** and **Raspberry Pi Pico** as motor controllers.

This workspace handles hardware communication, Lidar integration, 2D SLAM Mapping, and autonomous navigation (Nav2).

---

## 📂 1. Project Structure

- **`src/mbot_description/`**: The main robot package.
  - **`urdf/`**: Contains `mbot.xacro` (3D kinematic model).
  - **`launch/`**: Unified launch files for mapping, navigation, and teleop.
  - **`scripts/`**: `robot_bridge.py` (Universal hardware interface).
- **`fimware/`**:
  - **`ROSArduinoBridge/`**: High-performance firmware for **Arduino Nano**.
  - **`PicoRosBridge/`**: Optimized firmware for **Raspberry Pi Pico**.

---

## 🛠️ 2. Hardware Setup

### 🔌 Controller Options
1.  **Arduino Nano**: Use the firmware in `fimware/ROSArduinoBridge`. Optimized for Pins 2, 3, A4, A5 (Encoders).
2.  **Pi Pico**: Use the firmware in `fimware/PicoRosBridge`. Supports 4WD skid-steering on GP Pins.

### 🔌 Serial Permissions
```bash
# Give read/write permissions to your controller (usually ttyUSB0 or ttyACM0)
sudo chmod a+rw /dev/ttyUSB0
sudo chmod a+rw /dev/ttyUSB1
```

---

## 🏗️ 3. Installation & Building

```bash
cd ~/mbot
colcon build --symlink-install
source install/setup.bash
```

---

## 🏎️ 4. Quick Start: Drive the Robot

**Terminal 1:** Launch the robot.
```bash
source install/setup.bash
# For Nano (usually USB0):
ros2 launch mbot_description teleop_hardware.launch.py serial_port:=/dev/ttyUSB0

# For Pico (usually ACM0):
ros2 launch mbot_description teleop_hardware.launch.py serial_port:=/dev/ttyACM0
```

**Terminal 2:** Keyboard controller.
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

## 🗺️ 5. SLAM & Navigation

### Mapping:
```bash
ros2 launch mbot_description mapping.launch.py serial_port:=/dev/ttyUSB0
```

### Navigation:
```bash
ros2 launch mbot_description navigation.launch.py map:=/path/to/map.yaml serial_port:=/dev/ttyUSB0
```

---

## 🏢 Company Details & Copyright

**Company Name:** HUMYNEX ROBOTICS  
&copy; 2026 HUMYNEX ROBOTICS. All rights reserved.
