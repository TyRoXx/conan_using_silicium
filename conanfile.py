from conans import ConanFile, CMake

class ConanUsingSilicium(ConanFile):
	settings = "os", "compiler", "build_type", "arch"
	requires = "silicium/0.1@tyroxx/testing"
	generators = "cmake"
	default_options = "Boost:shared=True"
