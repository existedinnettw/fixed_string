# from conans import ConanFile, CMake
from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.build import check_min_cppstd, can_run
from conan.errors import ConanInvalidConfiguration


class FixedStringConan(ConanFile):
    name = "fixed_string"
    version = "1.0"
    license = "MIT License"
    author = "Daniil Dudkin"
    url = "https://github.com/unterumarmung/fixed_string"
    description = "C++ library that provides a basic_fixed_string template that combines std::array fixed-size semantic and std::string semantic together"
    topics = ("cpp17", "string", "constexpr")
    settings = "os", "compiler", "build_type", "arch"
    options = {"build_tests": [True, False], "build_examples": [True, False]}
    default_options = {"build_tests": False, "build_examples": False}
    exports_sources = "CMakeLists.txt", "include/*"
    no_copy_source = True

    def source(self):
        self.run("git clone https://github.com/unterumarmung/fixed_string.git")

    def validate(self):
        check_min_cppstd(self, 17)
        if self.options.build_examples:
            raise ConanInvalidConfiguration(
                "example is not (yet) available for fixed_string"
            )

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)

        tc.variables["FIXED_STRING_OPT_BUILD_EXAMPLES"] = self.options.build_examples
        tc.variables["FIXED_STRING_OPT_BUILD_TESTS"] = self.options.build_tests

        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()
        if self.options.build_tests and (
            not self.conf.get("tools.build:skip_test", default=False) and can_run(self)
        ):
            print("Running tests...")
            cmake.test()

    def package(self):
        copy(self, "*.h", self.source_folder, self.package_folder)
        copy(self, "*.hpp", self.source_folder, self.package_folder)

    def package_info(self):
        # self.cpp_info.libs = ["fixed_string"]
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []

    def package_id(self):
        self.info.clear()
