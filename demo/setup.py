# gmpyx_demo is not supported. It is included soley to test the
# exported C API.

from setuptools import Extension, setup
import sys
import os
import platform
import gmpyx

gmpyx_packagedir = os.path.dirname(gmpyx.__file__)
library_dirs = sys.path + [gmpyx_packagedir]
libnames = ['mpc','mpfr','gmp']

bundled_libs = os.path.join(gmpyx_packagedir, '..', 'gmpyx.libs')
if os.path.isdir(bundled_libs):
    library_dirs += [bundled_libs]
    if platform.system() == 'Linux':
        libnames = [':' + d for d in os.listdir(bundled_libs)]
    elif platform.system() == 'Darwin':
        libnames = [':' + bundled_libs + d for d in os.listdir(bundled_libs)]


gmpyx_ext = [
    Extension("gmpyx_demo", sources=["gmpyx_demo.c"],
              include_dirs=sys.path + [gmpyx_packagedir],
              library_dirs=library_dirs,
              libraries=libnames)]

setup (name = "gmpyx_demo",
       version = "0.3",
       description = "gmpyx_demo: gmpyx demonstration programs",
       author = "Case Van Horsen",
       url = "https://github.com/casevh/gmpyx",
       ext_modules = gmpyx_ext
)
