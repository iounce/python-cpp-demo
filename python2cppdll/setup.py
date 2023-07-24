from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("_python_trader_api",
                libraries=['thosttraderapi_se'],
                sources=["python_api_wrap.cxx"],)

setup(name="python_trader_api",
      version="0.1",
      description="swig extension demo",
      py_modules="python_trader_api",
      ext_modules=cythonize(ext))
