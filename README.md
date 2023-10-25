<div align="center">

<img src="docs/assets/icon.png" width="60" height="60" alt="logo">

# PyDjinni - Project Template

![GitHub](https://img.shields.io/github/license/pydjinni/pydjinni-project-template)

Project template using PyDjinni with Conan and CMake to build a library for multiple different target systems.

</div>

## Build Instructions

- Install the Python dependencies:
  ```sh
  pip install -r requirements.txt
  ```
- Run the PyDjinni package commands to build for Android, iOS and macOS:
  ```sh
  pydjinni package aar android
  pydjinni package swiftpackage ios ios_simulator macos
  ```