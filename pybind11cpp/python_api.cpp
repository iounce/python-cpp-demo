#include <pybind11/pybind11.h>
#include "python_func.h"
#include "python_bird.h"
#include "python_class.h"

namespace py = pybind11;

PYBIND11_MODULE(pybind11_demo, m)
{
    initFunc(m);
    initBird(m);
    initClass(m);
}