from conans import ConanFile

class LabVIEWBuild(ConanFile):
    requires = "labview_conan_poc_liba/[~=0.*]@intersoft/stable", "labview_conan_poc_libb/[~=0.*]@intersoft/stable"
    python_requires = "labview_conan_extension/[~=20.0.*]@intersoft/stable"
    python_requires_extend = "labview_conan_extension.LabVIEWConanExtension"