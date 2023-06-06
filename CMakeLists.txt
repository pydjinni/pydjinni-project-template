cmake_minimum_required(VERSION 3.24)

project(PyDjinniProjectTemplate)

# TODO load PyDjinni dynamically from github with FetchContent
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/modules")
Include(FetchContent)
Include(CTest)
Include(PyDjinni)

FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG        v3.3.2
)

if(BUILD_TESTING)
    FetchContent_MakeAvailable(Catch2)
    include(Catch)
endif()

if(ANDROID)
    find_package(Java 1.8 REQUIRED)
    include(UseJava)
    set(JAVA_AWT_LIBRARY NotNeeded)
    set(JAVA_AWT_INCLUDE_PATH NotNeeded)
    find_package(JNI REQUIRED)
endif()

add_subdirectory(lib)

if(BUILD_TESTING)
    add_subdirectory(test)
endif()
