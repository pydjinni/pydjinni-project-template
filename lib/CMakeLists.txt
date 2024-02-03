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
    LANGUAGES cpp java objc cppcli
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
    )
    foreach(CONFIGURATION_TYPE ${CMAKE_CONFIGURATION_TYPES})
        string(TOUPPER ${CONFIGURATION_TYPE} CONFIGURATION_TYPE)
        set_target_properties(PyDjinniLibrary PROPERTIES
            LIBRARY_OUTPUT_DIRECTORY_${CONFIGURATION_TYPE} .
        )
    endforeach()
    target_link_libraries(PyDjinniLibrary PRIVATE PyDjinniLibrary::Cpp)
    install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/PydjinniLibrary.framework.dSYM DESTINATION dist)
elseif(ANDROID)
    find_package(Java 1.8 REQUIRED)
    include(UseJava)
    set(JAVA_AWT_LIBRARY NotNeeded)
    set(JAVA_AWT_INCLUDE_PATH NotNeeded)
    find_package(JNI REQUIRED)
    add_library(PyDjinniLibrary SHARED ${jni_GENERATED_SOURCES})
    target_include_directories(PyDjinniLibrary PRIVATE ${jni_INCLUDE_DIR})
    target_link_libraries(PyDjinniLibrary PRIVATE JNI::JNI PyDjinniLibrary::Cpp)
    install(DIRECTORY ${java_SOURCE_DIR} DESTINATION dist/PyDjinniLibrary)
elseif(CMAKE_SYSTEM_NAME STREQUAL "Windows")
    add_library(PyDjinniLibrary SHARED ${cppcli_GENERATED_SOURCES} ${cppcli_GENERATED_HEADERS})
    target_include_directories(PyDjinniLibrary PUBLIC ${cppcli_INCLUDE_DIR})
    set_target_properties(PyDjinniLibrary PROPERTIES
        COMMON_LANGUAGE_RUNTIME "netcore"
        DOTNET_TARGET_FRAMEWORK "net8.0"
        DOTNET_SDK "Microsoft.NET.Sdk"
    )
    target_compile_options(PyDjinniLibrary PRIVATE /doc)
    foreach(CONFIGURATION_TYPE ${CMAKE_CONFIGURATION_TYPES})
        string(TOUPPER ${CONFIGURATION_TYPE} CONFIGURATION_TYPE)
        set_target_properties(PyDjinniLibrary PROPERTIES
            PDB_OUTPUT_DIRECTORY_${CONFIGURATION_TYPE} ${CMAKE_BINARY_DIR}/dist
            LIBRARY_OUTPUT_DIRECTORY_${CONFIGURATION_TYPE} ${CMAKE_BINARY_DIR}/dist
            RUNTIME_OUTPUT_DIRECTORY_${CONFIGURATION_TYPE} ${CMAKE_BINARY_DIR}/dist
        )
    endforeach()
    target_link_libraries(PyDjinniLibrary PRIVATE PyDjinniLibrary::Cpp)
endif()

set_target_properties(PyDjinniLibrary PROPERTIES
    EXCLUDE_FROM_ALL TRUE
)
install(TARGETS PyDjinniLibrary DESTINATION dist)