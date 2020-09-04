import os

from conans import CMake, ConanFile, tools


class IgnitionMsgsConan(ConanFile):
    name = "ignition-msgs"
    license = "Apache-2.0"
    author = "Juan Oxoby me@jmoxo.by"
    url = "https://github.com/ignitionrobotics/ign-msgs"
    description = "Protobuf messages and functions for robot applications."
    topics = ("ignition", "robotics", "gazebo", "protobuf", "messages")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake", "cmake_find_package_multi"
    exports_sources = ['patches/*']

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("ign-msgs-ignition-msgs5_5.3.0", self._source_subfolder)

    def requirements(self):
        for req in self.conan_data["requirements"]:
            self.requires(req)
        self.options["tinyxml2"].shared = self.options.shared

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        for patch in self.conan_data["patches"].get(self.version, []):
            tools.patch(**patch)

        self._install_ign_cmake()
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.name = f"ignition-msgs5"
        self.cpp_info.includedirs = [f"include/ignition/msgs5"]

    def _install_ign_cmake(self):
        # Get and build ign-cmake. This is just a set of cmake macros used by all the ignition
        # packages.
        self.run("git clone --depth=1 https://github.com/ignitionrobotics/ign-cmake.git --branch ignition-cmake2_2.4.0")
        cmake = CMake(self)
        cmake.configure(source_folder="ign-cmake", build_folder="build_ign-cmake")
        cmake.build()
        cmake.install()
