cmake_minimum_required(VERSION 3.8)
project(kratos_srushti)

find_package(ament_cmake REQUIRED)

install(
  PROGRAMS
    src/rover_status_publisher.py
    src/rover_status_subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
