from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.env import Environment


class SystemCAMSConan(ConanFile):
	name = "systemc-ams"
	version = "1.0"
	package_type = "application"

	settings = "os", "compiler", "build_type", "arch"
	exports_sources = "*"
	options = {"shared": [True, False], "fPIC": [True, False]}
	default_options = {"shared": True, "fPIC": False}

	def requirements(self):
		self.requires("systemc/3.0.1")

	def layout(self):
		self.folders.source = "."
		self.folders.build = "build"
		self.folders.generators = "build/generators"

	def generate(self):
		deps = CMakeDeps(self)
		deps.generate()
		tc = CMakeToolchain(self)
		tc.user_presets_path = 'CMakePresets.json'
		tc.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def config_options(self):
		if self.settings.os == "Windows":
			del self.options.fPIC
			self.options.shared=True

	def configure(self):
		if self.options.shared:
			self.options.rm_safe("fPIC")
			self.options["systemc/*"].shared = True
		else:
			self.options["systemc/*"].shared = False

	def package(self):
		pass

#	def package_info(self):
#		self.cpp_info.libs = ["sigma-delta"]
