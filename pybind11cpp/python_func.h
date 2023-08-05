#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "func.h"

namespace py = pybind11;

void initFunc(py::module &m)
{
    m.def("add", &Add<int>, "add int");
    m.def("add", &Add<double>, "add double");
    m.def("add", &Add<std::string>, "add string");
}