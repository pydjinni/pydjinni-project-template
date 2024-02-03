from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps


class PyDjinniLibraryRecipe(ConanFile):
    name = "PyDjinniLibrary"
    version = "1.0"
    package_type = "library"

    # Optional metadata
    license = "Apache 2.0"
    author = "pydjinni"
    description = "Example package using pydjinni for building a cross-platform library"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    test_requires = "catch2/3.5.2"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build(target="PyDjinniLibrary")
        cmake.install()

    

