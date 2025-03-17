from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps


class PyDjinniLibraryRecipe(ConanFile):
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    requires = "ms-gsl/4.1.0"
    test_requires = "catch2/3.7.0"
    build_requires = "cmake/3.31.5"

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
