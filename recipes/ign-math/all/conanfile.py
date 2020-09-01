import os

from conans import CMake, ConanFile, tools


class IgnMathConan(ConanFile):
    name = "ignition-math"
    version = "6.4.0"
    license = "<Put the package license here>"
    author = "Juan Oxoby me@jmoxo.by"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of IgnCmake here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake", "cmake_find_package"
    # build_requires = "ignition-cmake/2.4.0"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename(f"ign-math-ignition-math6_6.4.0", self._source_subfolder)

    def requirements(self):
        for req in self.conan_data["requirements"]:
            self.requires(req)

    def _configure_cmake(self):
        cmake = CMake(self)
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
        self.cpp_info.name = "ignition-math6"
        self.cpp_info.includedirs = ['include/ignition/math6']

    def _install_ign_cmake(self):
        # Get and build ign-cmake. This is just a set of cmake macros used by all the ignition
        # packages.
        self.run("git clone --depth=1 https://github.com/ignitionrobotics/ign-cmake.git --branch ignition-cmake2_2.4.0")
        cmake = CMake(self)
        cmake.configure(source_folder="ign-cmake", build_folder="build_ign-cmake")
        cmake.build()
        cmake.install()
