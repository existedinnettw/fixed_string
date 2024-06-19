cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(fixed_string CONFIG REQUIRED)

add_executable(test_package test_package.cpp)
target_link_libraries(test_package fixed_string::fixed_string)