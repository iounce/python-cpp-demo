from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(name="pybind11_demo",
                sources=["python_api.cpp"],
                include_dirs=["D:\\Application\\Python\\Python310\\Lib\\site-packages\\pybind11\\include"],
                language="c++")

setup(name="pybind11_demo",
      version="0.1",
      description="pybind11 extension demo",
      py_modules="pybind11_demo",
      ext_modules=cythonize(ext))
