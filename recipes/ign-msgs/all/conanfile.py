import os

from conans import CMake, ConanFile, tools


class IgnMsgsConan(ConanFile):
    name = "ignition-msgs"
    version = "5.3.0"
    license = "<Put the package license here>"
    author = "Juan Oxoby me@jmoxo.by"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of IgnCmake here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake", "cmake_find_package"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        # tools.get(**self.conan_data["sources"][self.version])
        self.run(f"cp -r /home/juan/ignition_workspace/src/ign-msgs {self._source_subfolder}")
        #os.rename("ign-msgs-ignition-msgs5_5.3.0", self._source_subfolder)

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

    def _install_ign_cmake(self):
        # Get and build ign-cmake. This is just a set of cmake macros used by all the ignition
        # packages.
        self.run("git clone --depth=1 https://github.com/ignitionrobotics/ign-cmake.git --branch ignition-cmake2_2.4.0")
        cmake = CMake(self)
        cmake.configure(source_folder="ign-cmake", build_folder="build_ign-cmake")
        cmake.build()
        cmake.install()
