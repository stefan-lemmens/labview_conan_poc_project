from conans import ConanFile

class LabVIEWBuild(ConanFile):
    requires = "labview_conan_poc_liba/[~=0.*]@user/stable", "labview_conan_poc_libb/[~=0.*]@user/stable"
    python_requires = "labview_conan_extension/[~=0.0.*]@user/stable"
    python_requires_extend = "labview_conan_extension.LabVIEWConanExtension"