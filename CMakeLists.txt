cmake_minimum_required(VERSION 3.16)

set(OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
set(LIB_OUTPUT_DIR "${CMAKE_BINARY_DIR}/lib")

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(${PROJECT} esp-template-project LANGUAGES C CXX)
