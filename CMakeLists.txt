cmake_minimum_required(VERSION 3.24)

project(PyDjinniProjectTemplate)

include(FetchContent)
FetchContent_Declare(pydjinni
        URL https://raw.githubusercontent.com/pydjinni/pydjinni/v1.0a2/cmake/modules/PyDjinni.cmake
        DOWNLOAD_NO_EXTRACT TRUE
)
FetchContent_MakeAvailable(pydjinni)
list(APPEND CMAKE_MODULE_PATH ${pydjinni_SOURCE_DIR})
include(PyDjinni)

FetchContent_Declare(
        Catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG        v3.3.2
)

option(BUILD_TESTING "Whether testing should be enabled or not" ON)

if(BUILD_TESTING)
    enable_testing()
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
