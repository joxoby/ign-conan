import glob
import os

from conans import CMake, ConanFile, tools


class IgnitionCmakeConan(ConanFile):
    name = "ignition-cmake"
    license = "Apache-2.0"
    author = "Juan Oxoby me@jmoxo.by"
    url = "https://github.com/ignitionrobotics/ign-cmake"
    description = "A set of CMake modules that are used by the C++-based Ignition projects."
    topics = ("ignition", "robotics", "cmake")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package_multi"

    @property
    def _major(self):
        return self.major_version

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename(f"ign-cmake-ignition-cmake2_2.4.0", self._source_subfolder)

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.name = f"ignition-cmake{self._major}"
        self.cpp_info.builddirs.append("share/cmake/ignition-cmake2/cmake2/")

        # Manually add all the cmake modules
        for file in glob.glob("./**/IgnCMake.cmake", recursive=True):
            print(file)
            self.cpp_info.build_modules.append(file)
