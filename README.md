<div align="center">

<img src="docs/assets/icon.png" width="60" height="60" alt="logo">

# PyDjinni - Project Template

![GitHub](https://img.shields.io/github/license/pydjinni/pydjinni-project-template)

Project template using PyDjinni with Conan and CMake to build a library for multiple different target systems.

</div>

## Prerequisites

### Android

- `ANDROID_HOME` must be set to an Android SDK installation on your device.
- `JAVA_HOME` must be set to a Java installation >= Java 17.

#### Windows

- `MinGW Makefiles` are used for the build. Install `MinGW` and make sure the `make` command (`mingw32-make`) is installed.

## Build Instructions

- Install the Python dependencies:
  ```sh
  pip install -r requirements.txt
  ```
- Run the PyDjinni package commands to build for Android, iOS, macOS and Windows:
  ```sh
  pydjinni package aar android
  pydjinni package swiftpackage ios ios_simulator macos
  pydjinni package nuget windows
  ```
  
## Unit Testing

Manually run the Unit-tests for the library (that test just the C++ code correctness):

### Linux, macOS:

```sh
conan install . --output-folder=build --build=missing
cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
cmake --build . --target tests
ctest --output-on-failure
```

### Windows:

```sh
conan install . --output-folder=build --build=missing
cd build
# assuming Visual Studio 17 2022 is your VS version and that it matches your default profile
cmake .. -G "Visual Studio 17 2022" -DCMAKE_TOOLCHAIN_FILE="conan_toolchain.cmake"
cmake --build . --config Release --target tests
ctest --output-on-failure
```
