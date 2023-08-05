#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "bird.h"

namespace py = pybind11;

void initBird(py::module &m)
{
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