cmake_minimum_required(VERSION 2.8.11)
project(test_package CXX)

include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
conan_basic_setup()

find_package(ignition-cmake2)

include(IgnUtils)
include(IgnPackaging)
