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
    exports_sources = ['patches/*']
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True
    }

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("console_bridge-1.0.1", self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
