cmake_minimum_required(VERSION 3.24)

project(PyDjinniProjectTemplate)

option(BUILD_TESTING "Whether testing should be enabled or not" ON)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/modules)
find_package(PyDjinni)
include(PyDjinni)

if(BUILD_TESTING)
    enable_testing()
endif()

add_subdirectory(lib)

if(BUILD_TESTING)
    add_subdirectory(tests)
endif()
