from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name = "name",
    ext_module = [
        CppExtension("module_name", ["cpp_module_path e.g.)src/test/cpp"]),
        CppExtension("module_name", ["cpp_module_path"]),
        ],
    cmdclass = {
        "build_ext": BuildExtension
        }
)
