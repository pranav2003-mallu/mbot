cmake_minimum_required(VERSION 3.8)
# ==========================================
# 🏢 Company: HUMYNEX ROBOTICS
# ⚖️ Copyright: (c) 2026 HUMYNEX ROBOTICS. All rights reserved.
# ==========================================
project(mbot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

# Install Python scripts (The Bridge and Filter)
install(PROGRAMS
  scripts/robot_bridge.py
  scripts/fake_odom.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install Hardware and Config directories
install(DIRECTORY
  launch
  urdf
  meshes
  config
  rviz
  maps
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
