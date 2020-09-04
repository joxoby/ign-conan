import os

from conans import CMake, ConanFile, tools


class URDFDom(ConanFile):
    name = "urdfdom"
    license = "BSD"
    author = "Juan Oxoby me@jmoxo.by"
    url = "https://github.com/ros/urdfdom"
    description = "URDF parser"
    topics = ("robotics", "simulation")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package", "cmake_find_package_multi"
    exports_sources = ['patches/*']

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("urdfdom-1.0.4", self._source_subfolder)

    def requirements(self):
        for req in self.conan_data["requirements"]:
            self.requires(req)
        self.options["tinyxml"].with_stl = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        for patch in self.conan_data["patches"].get(self.version, []):
            tools.patch(**patch)

        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
