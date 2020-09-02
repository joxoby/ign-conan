import os

from conans import CMake, ConanFile, tools


class IgnMathConan(ConanFile):
    name = "ignition-math"
    version = "6.4.0" # TODO: Don't hardcode the version here! Use a config.yml
    license = "Apache-2.0"
    author = "Juan Oxoby me@jmoxo.by"
    url = "https://github.com/ignitionrobotics/ign-math"
    description = " Math classes and functions for robot applications"
    topics = ("ignition", "math", "robotics", "gazebo")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake", "cmake_find_package_multi"
    # TODO: find a way of using an ign-make Conan package as a build_requirement
    # build_requires = "ignition-cmake/2.4.0"
    major_version = version.split('.')[0]

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _major(self):
        return self.major_version

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        # TODO: find a more portable way to refer to this folder
        os.rename(f"ign-math-ignition-math6_6.4.0", self._source_subfolder)

    def requirements(self):
        for req in self.conan_data["requirements"]:
            self.requires(req)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        self._install_ign_cmake()
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.name = f"ignition-math{self._major}"
        self.cpp_info.includedirs = [f"include/ignition/math{self._major}"]

    def _install_ign_cmake(self):
        # Get and build ign-cmake. This is just a set of cmake macros used by all the ignition
        # packages.
        # TODO: find a way of using an ign-make Conan package as a build_requirement
        self.run("git clone --depth=1 https://github.com/ignitionrobotics/ign-cmake.git --branch ignition-cmake2_2.4.0")
        cmake = CMake(self)
        cmake.configure(source_folder="ign-cmake", build_folder="build_ign-cmake")
        cmake.build()
        cmake.install()
