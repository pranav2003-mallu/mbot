# File Tree: mbot

**Generated:** 18/03/2026, 20:50:24
**Root Path:** `/home/mallu/mbot`

```
├── 📁 fimware
│   ├── 📁 PicoRosBridge
│   │   ├── 📄 PicoRosBridge.ino
│   │   ├── 📝 README.md
│   │   ├── ⚡ commands.h
│   │   ├── ⚡ diff_controller.h
│   │   ├── ⚡ encoder_driver.h
│   │   ├── 📄 encoder_driver.ino
│   │   ├── ⚡ motor_driver.h
│   │   ├── 📄 motor_driver.ino
│   │   └── ⚡ sensors.h
│   └── 📁 ROSArduinoBridge
│       ├── 📄 ROSArduinoBridge.ino
│       ├── ⚡ commands.h
│       ├── ⚡ diff_controller.h
│       ├── ⚡ encoder_driver.h
│       ├── 📄 encoder_driver.ino
│       ├── ⚡ motor_driver.h
│       ├── 📄 motor_driver.ino
│       ├── ⚡ sensors.h
│       ├── ⚡ servos.h
│       └── 📄 servos.ino
├── 📁 install
│   ├── 📁 mbot_description
│   │   ├── 📁 lib
│   │   │   └── 📁 mbot_description
│   │   │       ├── 🐍 fake_odom.py
│   │   │       └── 🐍 pico_bridge.py
│   │   └── 📁 share
│   │       ├── 📁 ament_index
│   │       │   └── 📁 resource_index
│   │       │       ├── 📁 package_run_dependencies
│   │       │       │   └── 📄 mbot_description
│   │       │       ├── 📁 packages
│   │       │       │   └── 📄 mbot_description
│   │       │       └── 📁 parent_prefix_path
│   │       │           └── 📄 mbot_description
│   │       ├── 📁 colcon-core
│   │       │   └── 📁 packages
│   │       │       └── 📄 mbot_description
│   │       └── 📁 mbot_description
│   │           ├── 📁 cmake
│   │           │   ├── 📄 mbot_descriptionConfig-version.cmake
│   │           │   └── 📄 mbot_descriptionConfig.cmake
│   │           ├── 📁 config
│   │           │   ├── ⚙️ mapper_params_online_async.yaml
│   │           │   └── ⚙️ nav2_params.yaml
│   │           ├── 📁 environment
│   │           │   ├── 📄 ament_prefix_path.dsv
│   │           │   ├── 📄 ament_prefix_path.sh
│   │           │   ├── 📄 path.dsv
│   │           │   └── 📄 path.sh
│   │           ├── 📁 hook
│   │           │   ├── 📄 cmake_prefix_path.dsv
│   │           │   ├── 📄 cmake_prefix_path.ps1
│   │           │   └── 📄 cmake_prefix_path.sh
│   │           ├── 📁 launch
│   │           │   ├── 🐍 mapping.launch.py
│   │           │   ├── 🐍 navigation.launch.py
│   │           │   ├── 🐍 teleop_hardware.launch.py
│   │           │   └── 🐍 teleop_rviz.launch.py
│   │           ├── 📁 maps
│   │           ├── 📁 meshes
│   │           │   ├── 📄 base_link.stl
│   │           │   ├── 📄 front_left_wheel_1.stl
│   │           │   ├── 📄 front_right_wheel_1.stl
│   │           │   ├── 📄 lidar_1.stl
│   │           │   ├── 📄 rear_left_wheel_1.stl
│   │           │   └── 📄 rear_right_wheel_1.stl
│   │           ├── 📁 rviz
│   │           │   └── 📄 rviz.rviz
│   │           ├── 📁 urdf
│   │           │   ├── 📄 materials.xacro
│   │           │   └── 📄 mbot.xacro
│   │           ├── 📄 local_setup.bash
│   │           ├── 📄 local_setup.dsv
│   │           ├── 📄 local_setup.sh
│   │           ├── 📄 local_setup.zsh
│   │           ├── 📄 package.bash
│   │           ├── 📄 package.dsv
│   │           ├── 📄 package.ps1
│   │           ├── 📄 package.sh
│   │           ├── ⚙️ package.xml
│   │           └── 📄 package.zsh
│   ├── 📁 rplidar_ros
│   │   ├── 📁 lib
│   │   │   └── 📁 rplidar_ros
│   │   │       ├── 📄 rplidar_client
│   │   │       ├── 📄 rplidar_composition
│   │   │       └── 📄 rplidar_node
│   │   └── 📁 share
│   │       ├── 📁 ament_index
│   │       │   └── 📁 resource_index
│   │       │       ├── 📁 package_run_dependencies
│   │       │       │   └── 📄 rplidar_ros
│   │       │       ├── 📁 packages
│   │       │       │   └── 📄 rplidar_ros
│   │       │       └── 📁 parent_prefix_path
│   │       │           └── 📄 rplidar_ros
│   │       ├── 📁 colcon-core
│   │       │   └── 📁 packages
│   │       │       └── 📄 rplidar_ros
│   │       └── 📁 rplidar_ros
│   │           ├── 📁 cmake
│   │           │   ├── 📄 ament_cmake_export_dependencies-extras.cmake
│   │           │   ├── 📄 ament_cmake_export_include_directories-extras.cmake
│   │           │   ├── 📄 rplidar_rosConfig-version.cmake
│   │           │   └── 📄 rplidar_rosConfig.cmake
│   │           ├── 📁 environment
│   │           │   ├── 📄 ament_prefix_path.dsv
│   │           │   ├── 📄 ament_prefix_path.sh
│   │           │   ├── 📄 path.dsv
│   │           │   └── 📄 path.sh
│   │           ├── 📁 hook
│   │           │   ├── 📄 cmake_prefix_path.dsv
│   │           │   ├── 📄 cmake_prefix_path.ps1
│   │           │   └── 📄 cmake_prefix_path.sh
│   │           ├── 📁 launch
│   │           │   ├── 🐍 rplidar_a1_launch.py
│   │           │   └── 🐍 view_rplidar_a1_launch.py
│   │           ├── 📁 rviz
│   │           │   └── 📄 rplidar_ros.rviz
│   │           ├── 📄 local_setup.bash
│   │           ├── 📄 local_setup.dsv
│   │           ├── 📄 local_setup.sh
│   │           ├── 📄 local_setup.zsh
│   │           ├── 📄 package.bash
│   │           ├── 📄 package.dsv
│   │           ├── 📄 package.ps1
│   │           ├── 📄 package.sh
│   │           ├── ⚙️ package.xml
│   │           └── 📄 package.zsh
│   ├── ⚙️ .colcon_install_layout
│   ├── 📄 COLCON_IGNORE
│   ├── 🐍 _local_setup_util_ps1.py
│   ├── 🐍 _local_setup_util_sh.py
│   ├── 📄 local_setup.bash
│   ├── 📄 local_setup.ps1
│   ├── 📄 local_setup.sh
│   ├── 📄 local_setup.zsh
│   ├── 📄 setup.bash
│   ├── 📄 setup.ps1
│   ├── 📄 setup.sh
│   └── 📄 setup.zsh
├── 📁 log
│   ├── 📁 build_2026-03-18_12-12-38
│   │   ├── 📁 mbot_description
│   │   └── 📁 rplidar_ros
│   ├── 📁 build_2026-03-18_13-01-57
│   │   ├── 📁 mbot_description
│   │   └── 📁 rplidar_ros
│   ├── 📄 COLCON_IGNORE
│   ├── 📄 latest
│   └── 📄 latest_build
├── 📁 src
│   ├── 📁 mbot_description
│   │   ├── 📁 config
│   │   │   ├── ⚙️ mapper_params_online_async.yaml
│   │   │   └── ⚙️ nav2_params.yaml
│   │   ├── 📁 include
│   │   │   └── 📁 mbot_description
│   │   ├── 📁 launch
│   │   │   ├── 🐍 mapping.launch.py
│   │   │   ├── 🐍 navigation.launch.py
│   │   │   ├── 🐍 teleop_hardware.launch.py
│   │   │   └── 🐍 teleop_rviz.launch.py
│   │   ├── 📁 maps
│   │   ├── 📁 meshes
│   │   │   ├── 📄 base_link.stl
│   │   │   ├── 📄 front_left_wheel_1.stl
│   │   │   ├── 📄 front_right_wheel_1.stl
│   │   │   ├── 📄 lidar_1.stl
│   │   │   ├── 📄 rear_left_wheel_1.stl
│   │   │   └── 📄 rear_right_wheel_1.stl
│   │   ├── 📁 rviz
│   │   │   └── 📄 rviz.rviz
│   │   ├── 📁 scripts
│   │   │   ├── 🐍 fake_odom.py
│   │   │   └── 🐍 robot_bridge.py
│   │   ├── 📁 src
│   │   ├── 📁 urdf
│   │   │   ├── 📄 materials.xacro
│   │   │   └── 📄 mbot.xacro
│   │   ├── 📄 CMakeLists.txt
│   │   └── ⚙️ package.xml
│   └── 📁 rplidar_ros
│       ├── 📁 debian
│       │   └── 📄 udev
│       ├── 📁 include
│       │   ├── ⚡ rplidar_node.hpp
│       │   └── ⚡ visibility.h
│       ├── 📁 launch
│       │   ├── 🐍 rplidar_a1_launch.py
│       │   └── 🐍 view_rplidar_a1_launch.py
│       ├── 📁 rviz
│       │   └── 📄 rplidar_ros.rviz
│       ├── 📁 scripts
│       │   ├── 📄 create_udev_rules.sh
│       │   ├── 📄 delete_udev_rules.sh
│       │   └── 📄 rplidar.rules
│       ├── 📁 sdk
│       │   ├── 📁 include
│       │   │   ├── ⚡ rplidar.h
│       │   │   ├── ⚡ rplidar_cmd.h
│       │   │   ├── ⚡ rplidar_driver.h
│       │   │   ├── ⚡ rplidar_protocol.h
│       │   │   ├── ⚡ rptypes.h
│       │   │   ├── ⚡ sl_crc.h
│       │   │   ├── ⚡ sl_lidar.h
│       │   │   ├── ⚡ sl_lidar_cmd.h
│       │   │   ├── ⚡ sl_lidar_driver.h
│       │   │   ├── ⚡ sl_lidar_driver_impl.h
│       │   │   ├── ⚡ sl_lidar_protocol.h
│       │   │   └── ⚡ sl_types.h
│       │   ├── 📁 src
│       │   │   ├── 📁 arch
│       │   │   │   ├── 📁 linux
│       │   │   │   │   ├── ⚡ arch_linux.h
│       │   │   │   │   ├── ⚡ net_serial.cpp
│       │   │   │   │   ├── ⚡ net_serial.h
│       │   │   │   │   ├── ⚡ net_socket.cpp
│       │   │   │   │   ├── ⚡ thread.hpp
│       │   │   │   │   ├── ⚡ timer.cpp
│       │   │   │   │   └── ⚡ timer.h
│       │   │   │   ├── 📁 macOS
│       │   │   │   │   ├── ⚡ arch_macOS.h
│       │   │   │   │   ├── ⚡ net_serial.cpp
│       │   │   │   │   ├── ⚡ net_serial.h
│       │   │   │   │   ├── ⚡ net_socket.cpp
│       │   │   │   │   ├── ⚡ thread.hpp
│       │   │   │   │   ├── ⚡ timer.cpp
│       │   │   │   │   └── ⚡ timer.h
│       │   │   │   └── 📁 win32
│       │   │   │       ├── ⚡ arch_win32.h
│       │   │   │       ├── ⚡ net_serial.cpp
│       │   │   │       ├── ⚡ net_serial.h
│       │   │   │       ├── ⚡ net_socket.cpp
│       │   │   │       ├── ⚡ timer.cpp
│       │   │   │       ├── ⚡ timer.h
│       │   │   │       └── ⚡ winthread.hpp
│       │   │   ├── 📁 dataunpacker
│       │   │   │   ├── 📁 unpacker
│       │   │   │   │   ├── ⚡ handler_capsules.cpp
│       │   │   │   │   ├── ⚡ handler_capsules.h
│       │   │   │   │   ├── ⚡ handler_hqnode.cpp
│       │   │   │   │   ├── ⚡ handler_hqnode.h
│       │   │   │   │   ├── ⚡ handler_normalnode.cpp
│       │   │   │   │   └── ⚡ handler_normalnode.h
│       │   │   │   ├── ⚡ dataunnpacker_commondef.h
│       │   │   │   ├── ⚡ dataunnpacker_internal.h
│       │   │   │   ├── ⚡ dataunpacker.cpp
│       │   │   │   ├── ⚡ dataunpacker.h
│       │   │   │   └── ⚡ dataupacker_namespace.h
│       │   │   ├── 📁 hal
│       │   │   │   ├── ⚡ abs_rxtx.h
│       │   │   │   ├── ⚡ assert.h
│       │   │   │   ├── ⚡ byteops.h
│       │   │   │   ├── ⚡ byteorder.h
│       │   │   │   ├── ⚡ event.h
│       │   │   │   ├── ⚡ locker.h
│       │   │   │   ├── ⚡ socket.h
│       │   │   │   ├── ⚡ thread.cpp
│       │   │   │   ├── ⚡ thread.h
│       │   │   │   ├── ⚡ types.h
│       │   │   │   ├── ⚡ util.h
│       │   │   │   └── ⚡ waiter.h
│       │   │   ├── ⚡ rplidar_driver.cpp
│       │   │   ├── ⚡ sdkcommon.h
│       │   │   ├── ⚡ sl_async_transceiver.cpp
│       │   │   ├── ⚡ sl_async_transceiver.h
│       │   │   ├── ⚡ sl_crc.cpp
│       │   │   ├── ⚡ sl_lidar_driver.cpp
│       │   │   ├── ⚡ sl_lidarprotocol_codec.cpp
│       │   │   ├── ⚡ sl_lidarprotocol_codec.h
│       │   │   ├── ⚡ sl_serial_channel.cpp
│       │   │   ├── ⚡ sl_tcp_channel.cpp
│       │   │   └── ⚡ sl_udp_channel.cpp
│       │   └── 📄 Makefile
│       ├── 📁 src
│       │   ├── ⚡ rplidar_client.cpp
│       │   └── ⚡ rplidar_node.cpp
│       ├── ⚙️ .gitignore
│       ├── 📄 CHANGELOG.rst
│       ├── 📄 CMakeLists.txt
│       ├── 📄 LICENSE
│       ├── 📝 README.md
│       ├── ⚙️ package.xml
│       └── 🖼️ rplidar_A1.png
└── 📝 readme.md
```

---
*Generated by FileTree Pro Extension*