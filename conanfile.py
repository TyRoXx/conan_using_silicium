from conans import ConanFile, CMake

class ConanUsingSilicium(ConanFile):
	settings = "os", "compiler", "build_type", "arch"
	requires = "Boost/1.59.0@lasote/stable", "silicium/0.1@tyroxx/testing"
	generators = "cmake"
	default_options = "Boost:shared=True"
