import os

from conans import CMake, ConanFile, tools


class ConsoleBridge(ConanFile):
    name = "console_bridge"
    license = "BSD-3"
    author = "Juan Oxoby me@jmoxo.by"
    url = "https://github.com/ros/console_bridge"
    description = "A ROS-independent package for logging that seamlessly pipes into rosconsole/rosout for ROS-dependent packages."
    topics = ("robotics", "simulation")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package_multi"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("console_bridge-1.0.1", self._source_subfolder)

    def requirements(self):
        pass
        # for req in self.conan_data["requirements"]:
        #     self.requires(req)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        pass
