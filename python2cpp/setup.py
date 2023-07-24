from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(name="python_cpp_demo",
                sources=["python_rect.pyx", "rect.cpp"],
                language="c++")

setup(name="python_cpp_demo",
      version="0.1",
      description="cpp extension demo",
      py_modules="python_cpp_demo",
      ext_modules=cythonize(ext))
