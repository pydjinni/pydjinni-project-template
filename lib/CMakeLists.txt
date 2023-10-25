
set(PROJECT_LANGUAGES CXX)
set(DARWIN_SYSTEM "Darwin;iOS")
if(CMAKE_SYSTEM_NAME IN_LIST DARWIN_SYSTEM)
  list(APPEND PROJECT_LANGUAGES OBJC OBJCXX)
elseif(ANDROID)
    list(APPEND PROJECT_LANGUAGES C)
endif()

project(PyDjinniProjectTemplateLibrary LANGUAGES ${PROJECT_LANGUAGES})

pydjinni_generate(interface.pydjinni 
    CONFIG ${CMAKE_SOURCE_DIR}/pydjinni.yaml
    LANGUAGES cpp java objc
    CLEAN
)

add_library(CppPyDjinniLibrary STATIC
    ${cpp_GENERATED_HEADERS}
    ${cpp_GENERATED_SOURCES}
        src/hello_world.cpp
)
add_library(PyDjinniLibrary::Cpp ALIAS CppPyDjinniLibrary)
target_include_directories(CppPyDjinniLibrary PUBLIC ${cpp_INCLUDE_DIR})
target_compile_features(CppPyDjinniLibrary PUBLIC cxx_std_20)
set_target_properties(CppPyDjinniLibrary PROPERTIES
        CXX_STANDARD 20
        CXX_STANDARD_REQUIRED true
        CXX_EXTENSIONS false
        POSITION_INDEPENDENT_CODE TRUE
)

if(CMAKE_SYSTEM_NAME IN_LIST DARWIN_SYSTEM)
    add_library(PyDjinniLibrary SHARED ${objc_GENERATED_SOURCES} ${objcpp_GENERATED_SOURCES} ${objc_GENERATED_HEADERS})
    target_include_directories(PyDjinniLibrary PUBLIC ${objc_INCLUDE_DIR} PRIVATE ${objcpp_INCLUDE_DIR})
    set_target_properties(PyDjinniLibrary PROPERTIES
        FRAMEWORK TRUE
        MACOSX_FRAMEWORK_IDENTIFIER pydjinni.template
        PUBLIC_HEADER "${objc_GENERATED_HEADERS}"
        XCODE_ATTRIBUTE_DEFINES_MODULE YES
        XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC YES
        XCODE_ATTRIBUTE_DEBUG_INFORMATION_FORMAT dwarf-with-dsym
        LIBRARY_OUTPUT_DIRECTORY_DEBUG .
        LIBRARY_OUTPUT_DIRECTORY_RELEASE .
    )
    target_link_libraries(PyDjinniLibrary PRIVATE PyDjinniLibrary::Cpp)
    install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/PydjinniLibrary.framework.dSYM DESTINATION dist)
elseif(ANDROID)
    add_library(PyDjinniLibrary SHARED ${jni_GENERATED_SOURCES})
    target_include_directories(PyDjinniLibrary PRIVATE ${jni_INCLUDE_DIR})
    target_link_libraries(PyDjinniLibrary PRIVATE JNI::JNI PyDjinniLibrary::Cpp)
    add_jar(JavaPyDjinniLibrary
        SOURCES ${java_GENERATED_SOURCES}
        OUTPUT_NAME PyDjinniLibrary
    )
    add_dependencies(PyDjinniLibrary JavaPyDjinniLibrary)
    install_jar(JavaPyDjinniLibrary dist)
endif()

install(TARGETS PyDjinniLibrary DESTINATION dist)