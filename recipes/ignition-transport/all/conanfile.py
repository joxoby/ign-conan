import os

from conans import CMake, ConanFile, tools


class IgnitionTransportConan(ConanFile):
    name = "ignition-transport"
    license = "Apache-2.0"
    author = "Juan Oxoby me@jmoxo.by"
    url = "https://github.com/ignitionrobotics/ign-transport"
    description = "A component of Ignition Robotics, provides fast and efficient \
                   asyncronous message passing, services, and data logging."
    topics = ("ignition", "pubsub", "gazebo", "robotics", "zmq")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True, "zeromq:shared": True}
    generators = "cmake", "cmake_find_package_multi"

    @property
    def _major(self):
        return self.major_version

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("ign-transport-ignition-transport8_8.1.0", self._source_subfolder)

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
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.name = "ignition-transport8"
        self.cpp_info.includedirs = ['include/ignition/transport8']

    def _install_ign_cmake(self):
        # Get and build ign-cmake. This is just a set of cmake macros used by all the ignition
        # packages.
        # self.run("cp -ar ~/ignition_workspace/src/ign-cmake ign-cmake")
        self.run("git clone --depth=1 https://github.com/joxoby/ign-cmake.git --branch add_config_search_for_tinyxml2")
        cmake = CMake(self)
        cmake.configure(source_folder="ign-cmake", build_folder="build_ign-cmake")
        cmake.build()
        cmake.install()
