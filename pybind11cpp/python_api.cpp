#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
namespace py = pybind11;

#include "func.h"
#include "bird.h"

PYBIND11_MODULE(pybind11_demo, m)
{
    m.def("add", &Add<int>, "add int");
    m.def("add", &Add<double>, "add double");
    m.def("add", &Add<std::string>, "add string");

    py::class_<Animal>(m, "Animal")
        .def(py::init<>())
        .def(py::init<const std::string &>())
        .def("name", &Animal::GetName);

    py::class_<Bird, Animal>(m, "Bird")
        .def(py::init<>())
        .def(py::init<const std::string &>())
        .def("name", &Bird::GetName)
        .def("fly", &Bird::Fly);
}