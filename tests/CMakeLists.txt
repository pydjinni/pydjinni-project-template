project(PyDjinniProjectTemplateTests LANGUAGES CXX)

find_package(Catch2 REQUIRED)

add_executable(tests test.cpp)
target_link_libraries(tests PRIVATE Catch2::Catch2WithMain PyDjinniLibrary::Cpp)

include(Catch)
catch_discover_tests(tests)
