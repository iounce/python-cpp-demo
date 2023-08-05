#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "class.h"

namespace py = pybind11;

class PyBase: public Base
{
public:
    using Base::Base;

    bool valid() override
    {
        PYBIND11_OVERRIDE_PURE(
            bool,
            Base,
            valid,
        );
    }
};

class PyPublicBase: public Base
{
public:
    using Base::valid;
};

void initClass(py::module &m)
{
    py::class_<Base, PyBase>(m, "Base")
        .def(py::init<>())
        .def_readwrite_static("type", &Base::m_type)
        .def("set", py::overload_cast<int>(&Base::set), "set int value")
        .def("set", py::overload_cast<const std::string &>(&Base::set), "set string value")
        .def("parse", [](Base &self, std::vector<std::string> args)
            {
                std::vector<char *> ptrargs;
                ptrargs.reserve(args.size());
                for (auto &s : args) 
                {
                    ptrargs.push_back(const_cast<char *>(s.c_str()));
                }
                return self.parse(ptrargs.size(), ptrargs.data()); 
            })
        .def("valid", &PyPublicBase::valid);
}