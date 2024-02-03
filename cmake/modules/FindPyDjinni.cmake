include(FindPackageHandleStandardArgs)

find_package(Python3 REQUIRED COMPONENTS Interpreter)
execute_process(COMMAND ${Python3_EXECUTABLE} -c "import pydjinni; print(pydjinni.__path__[0])"
        OUTPUT_STRIP_TRAILING_WHITESPACE
        OUTPUT_VARIABLE PyDjinni_LIBRARY_DIR)
list(APPEND CMAKE_MODULE_PATH ${PyDjinni_LIBRARY_DIR}/cmake/modules)
find_package_handle_standard_args(PyDjinni
    REQUIRED_VARS
        PyDjinni_ROOT_DIR ${PyDjinni_LIBRARY_DIR}
)